#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division

import os
import sys
from functools import reduce
import numpy as np
import pandas as pd

currentPath = os.path.dirname(os.path.realpath(__file__))
py3Path = os.path.abspath(os.path.join(currentPath, '..'))
sys.path.append(py3Path)
from py3.constant import commonConst as coco
from py3.process import aggrLink as agg
from py3.process import save2Excel as s2e
from py3.process import transform as trans


# 准备源指标列聚合所需要用到的表
def preparedOriginTabDF(vehExDF, netCheckDF, fdWtDF, btWtDF, groupColName, *bakupNetCheckExcName):
    # 提取源指标列，按vehicle_id分组聚合，去重
    netCheckDF = netCheckDF[
        ['po_amount', 'fd_amount', 'bt_amount', 'gps_amount', 'gps_amount_his', 'gps_draft_amount', 'gps_total_amount',
         'mileage', 'mileage_total', 'alarm_ser_amount', 'alarm_ser_deal_amount']] \
        .groupby(netCheckDF['vehicle_id']) \
        .sum()
    netCheckDF.reset_index(inplace=True)

    # 过滤白名单
    netCheckDF = trans.filterWhite(vehExDF, netCheckDF, fdWtDF, btWtDF)

    if len(bakupNetCheckExcName) != 0:
        # 备份202001-当前月的总的netcheck数据(postNetCheck+currentNetCheck)到备份目录，待下个月复用
        s2e.backUpNetCheck(netCheckDF, bakupNetCheckExcName[0])

    # 关联车表
    vehLinkedDF = pd.merge(vehExDF, netCheckDF, on='vehicle_id', how='inner')

    # 提取指标聚合字段
    vehLinkedDF = vehLinkedDF[
        [groupColName,
         'po_amount', 'fd_amount', 'bt_amount', 'gps_amount', 'gps_amount_his', 'gps_draft_amount', 'gps_total_amount',
         'mileage', 'mileage_total', 'alarm_ser_amount', 'alarm_ser_deal_amount']]

    return vehLinkedDF, netCheckDF


# 生成风险指标,（groupby字段会自动变成index，若要提取该字段，务必reset_index）
def generateRiskRank(vehLinkedDF, netCheckDF, groupColName, dimTab, bt_flag):
    # 分组聚合指标，生成所有指标列的单列DF
    aggr = agg.quotaAggr(vehLinkedDF, netCheckDF, groupColName)
    quotaColAggrDFList = aggr.getQuotaColAggrDFList()

    # 拼表,得到风险排名总表
    riskRankBigTab = splicingTab(quotaColAggrDFList, groupColName, dimTab, bt_flag)

    # 重置列名和类型
    riskRankBigTab = reSetCols(riskRankBigTab)

    return riskRankBigTab


## 拼表，表的连接关系 riskRankBigTab = quotaTab + riskTab + jiangsuDF
def splicingTab(quotaColAggrDFList, groupColName, dimTab, bt_flag):
    # 拼接指标列，生成指标表
    quotaTab = reduce(lambda left, right: pd.merge(left, right, on=groupColName, how='outer'), quotaColAggrDFList)
    quotaTab.iloc[:, :].fillna(value=0.0, inplace=True)  # 填充空值为0.0，否则妨碍排序生成指表列

    # 生成风险值表
    riskTab = getRiskTab(quotaTab, groupColName, bt_flag)

    # 拼接指标表和风险值表,并按总风险值列降序排序
    quotaRiskTab = pd.merge(quotaTab, riskTab, on=groupColName, how='inner')
    quotaRiskTab = quotaRiskTab.sort_values(by='riskValueSum', ascending=False)  # DESC
    quotaRiskTab.reset_index(inplace=True)
    riskRankBigTab = quotaRiskTab

    # dimTab == 0表示没有传维表
    if groupColName == 'city_name' and dimTab == 0:
        # 添加city_name = '江苏省'一行，算法：不统计风险值列,只统计指标列
        jiangsuDF = getJiangsuDF(quotaTab, groupColName)

        # riskRankTab纵向合并jiangsuDF
        riskRankBigTab = pd.concat([quotaRiskTab, jiangsuDF], axis=0, ignore_index=True)

        # 用'/'填充江苏省风险值列
        riskRankBigTab.fillna(value='/', inplace=True)


    elif groupColName == 'company_name':
        # 关联维表，引入city_name列，company_name列、transport_mng_name列
        riskRankBigTab = pd.merge(quotaRiskTab, dimTab, on='company_name', how='inner')
        riskRankBigTab.sort_values(by='riskValueSum', ascending=False)  # 重新排序
        riskRankBigTab.reset_index(inplace=True)

    elif groupColName == 'transport_mng_name':
        # 关联维表，引入city_name列，transport_mng_name列
        riskRankBigTab = pd.merge(quotaRiskTab, dimTab, on='transport_mng_name', how='inner')
        riskRankBigTab.sort_values(by='riskValueSum', ascending=False)  # 重新排序
        riskRankBigTab.reset_index(inplace=True)

    else:
        print('groupColName非法，无法关联维表！！！')
        print('当前groupColName为 : ' + groupColName)
        exit(1)

    return riskRankBigTab


# 生成风险值表
def getRiskTab(quotaTab, groupColName, bt_flag):
    ## 生成风险值列
    riskValueDFList = getRiskValueDFList(quotaTab, groupColName)

    # 拼接风险值列
    riskTab = reduce(lambda left, right: pd.merge(left, right, on=groupColName, how='inner'), riskValueDFList)

    # 生成总风险值列
    riskValueColNames = riskTab.columns.values.tolist()
    if bt_flag == 1:
        riskValueColNames.remove(groupColName)
    else:
        # 逻辑上剔除夜间禁行风险值统计对排序的影响
        riskValueColNames.remove(groupColName)
        riskValueColNames.remove('bt_riskValue')
    riskTab['riskValueSum'] = riskTab[riskValueColNames].apply(lambda row: row.sum(), axis=1)

    return riskTab


def getJiangsuDF(quotaTab, groupColName):
    quotaCols = quotaTab.columns.values.tolist()
    quotaCols.remove(groupColName)
    # 简单聚合列
    simpleSumCols = ['veh_net', 'po_amount', 'fd_amount', 'bt_amount', 'veh_online', 'draft_amount', 'mileage',
                     'mileage_total', 'alarm_ser_amount', 'alarm_ser_deal_amount']
    simpleSumSeries = quotaTab[simpleSumCols].sum()

    # 复杂聚合列
    complexSumCols = ['avg_po_amount', 'avg_fd_amount', 'avg_bt_amount', 'line_rate', 'qualifi_rate', 'draft_rate',
                      'mileage_rate', 'alarm_ser_rate']
    complexSumRes = []
    avg_po_amount = quotaTab['po_amount'].sum() / quotaTab['veh_online'].sum()
    avg_fd_amount = quotaTab['fd_amount'].sum() / quotaTab['veh_online'].sum()
    avg_bt_amount = quotaTab['bt_amount'].sum() / quotaTab['veh_online'].sum()
    line_rate = quotaTab['veh_online'].sum() / quotaTab['veh_net'].sum()
    qualifi_rate = quotaTab['gps_amount'].sum() / quotaTab['gps_total_amount'].sum()
    draft_rate = quotaTab['draft_amount'].sum() / quotaTab['veh_online'].sum()
    mileage_rate = quotaTab['mileage'].sum() / quotaTab['mileage_total'].sum()
    alarm_ser_rate = quotaTab['alarm_ser_deal_amount'].sum() / quotaTab['alarm_ser_amount'].sum()
    complexSumRes.append(cut(avg_po_amount))
    complexSumRes.append(cut(avg_fd_amount))
    complexSumRes.append(cut(avg_bt_amount))
    complexSumRes.append(cut(line_rate))
    complexSumRes.append(cut(qualifi_rate))
    complexSumRes.append(cut(draft_rate))
    complexSumRes.append(cut(mileage_rate))
    complexSumRes.append(cut(alarm_ser_rate))
    complexSumSeries = pd.Series(complexSumRes, index=complexSumCols)

    # 拼接
    jiangsuSeries = pd.concat([simpleSumSeries, complexSumSeries])
    jiangsuDF = pd.DataFrame(jiangsuSeries)
    jiangsuDF = jiangsuDF.T  # 转置为一行
    jiangsuDF[groupColName] = '江苏省'
    return jiangsuDF


# 保留四位小数，不四舍五入
def cut(doubleNum):
    return int(doubleNum * 10000) / 10000.0


# 重置列名
def reSetCols(riskRankBigTab):
    # 重置列名
    constObj = coco.colNameConst()
    nameMap = constObj.getnameMap()
    riskRankBigTab.rename(columns=nameMap, inplace=True)

    # 重置数据类型为np.object
    riskRankBigTab = riskRankBigTab.astype(np.object)

    return riskRankBigTab


def getRiskValueDFList(quotaTab, groupColName):
    # 获取正反向指标列，dic {'依赖指标':'风险值'}
    quota = coco.quotaConst()
    negativeQuota = quota.getnegativeQuota()  # 反指标，以及对应的可生成的风险值列名
    positiveQuota = quota.getpositiveQuota()

    RiskValueDFList = []
    dependQuotaColNames = negativeQuota.keys()
    dependQuotaColNames.extend(positiveQuota.keys())
    dependQuotaColDFList = []
    for col in dependQuotaColNames:
        dependQuotaColDFList.append(quotaTab[[groupColName, col]])

    for colsDF in dependQuotaColDFList:
        colNames = colsDF.columns.values.tolist()
        quotaColName = colNames[1]

        # 按反向指标列生成风险值,反向指标数值越高，风险值越高
        if quotaColName in negativeQuota.keys():
            sortedDF = colsDF.sort_values(by=quotaColName, ascending=True)  # ASC
            sortedDF.reset_index(inplace=True)  # 重置索引

            # 新建风险值列，默认值为0.0
            riskValueColName = negativeQuota[quotaColName]
            sortedDF[riskValueColName] = 0.0
            quotaColIndex = sortedDF.columns.get_loc(quotaColName)
            riskValueColIndex = sortedDF.columns.get_loc(riskValueColName)

            # 给风险值列赋值
            riskValue = 0
            count = 0
            postQaotaValue = None
            quotaRowNum = len(sortedDF)
            for rowNum in range(0, quotaRowNum):
                count = count + 1
                currQuotaValue = cut(sortedDF.iloc[rowNum, quotaColIndex])  # 取指标值列的值
                if (postQaotaValue is None) and (riskValue == 0):  # 第一次循环
                    postQaotaValue = currQuotaValue
                    riskValue = 1
                    sortedDF.iloc[rowNum, riskValueColIndex] = riskValue
                else:
                    if currQuotaValue == postQaotaValue:
                        postQaotaValue = currQuotaValue
                        sortedDF.iloc[rowNum, riskValueColIndex] = riskValue
                    elif currQuotaValue > postQaotaValue:
                        riskValue = count
                        postQaotaValue = currQuotaValue
                        sortedDF.iloc[rowNum, riskValueColIndex] = riskValue
                    else:
                        print('指标列排序有误，程序终止！！！')
                        exit(1)

            RiskValueDFList.append(sortedDF[[groupColName, riskValueColName]])

        # 按正向指标列生成风险值,正向指标数值越高，风险值越低
        if quotaColName in positiveQuota.keys():
            sortedDF = colsDF.sort_values(by=quotaColName, ascending=False)  # DESC
            sortedDF.reset_index(inplace=True)  # 重置索引
            # 新建风险值列，默认值为0.0
            riskValueColName = positiveQuota[quotaColName]
            sortedDF[riskValueColName] = 0.0
            quotaColIndex = sortedDF.columns.get_loc(quotaColName)
            riskValueColIndex = sortedDF.columns.get_loc(riskValueColName)

            # 给风险值列赋值
            riskValue = 0
            count = 0
            postQaotaValue = None
            quotaRowNum = len(sortedDF)
            for rowNum in range(0, quotaRowNum):
                count = count + 1
                currQuotaValue = cut(sortedDF.iloc[rowNum, quotaColIndex])  # 取指标值列的值
                if (postQaotaValue is None) and (riskValue == 0):  # 第一次循环
                    # -------------------调测代码---------------------
                    # if quotaColName == 'qualifi_rate':
                    #     ci = sortedDF.iloc[rowNum, 1]
                    #     print('current_city_name:', ci, 'count:', count, 'riskValue:', riskValue, 'postQaotaValue:',
                    #           postQaotaValue, 'currQuotaValue:', currQuotaValue)
                    # ----------------------------------------------
                    postQaotaValue = currQuotaValue
                    riskValue = 1
                    sortedDF.iloc[rowNum, riskValueColIndex] = riskValue
                else:
                    # -------------------调测代码---------------------
                    # if quotaColName == 'qualifi_rate':
                    #     ci = sortedDF.iloc[rowNum, 1]
                    #     print('current_city_name:', ci, 'count:', count, 'riskValue:', riskValue, 'postQaotaValue:',
                    #           postQaotaValue, 'currQuotaValue:', currQuotaValue)
                    # ----------------------------------------------
                    if currQuotaValue == postQaotaValue:
                        postQaotaValue = currQuotaValue
                        sortedDF.iloc[rowNum, riskValueColIndex] = riskValue
                    elif currQuotaValue < postQaotaValue:
                        riskValue = count
                        postQaotaValue = currQuotaValue
                        sortedDF.iloc[rowNum, riskValueColIndex] = riskValue
                    else:
                        print('指标列排序有误，程序终止！！！')
                        exit(1)

            RiskValueDFList.append(sortedDF[[groupColName, riskValueColName]])

    return RiskValueDFList
