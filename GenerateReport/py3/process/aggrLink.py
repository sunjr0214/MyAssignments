#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
import pandas as pd


# if sys.getdefaultencoding() != 'utf-8':
#     reload(sys)
#     sys.setdefaultencoding('utf-8')

class quotaAggr(object):
    def __init__(self, linkDF, netCheckDF, groupColName):
        self.DF = linkDF
        # 原始netCheckDF
        self.netCheckDF = netCheckDF
        # 按该字段分组聚合
        self.groupColName = groupColName

    # 除计算，保留四位小数，不四舍五入
    def division(self, x, y):
        return 0.0 if y == 0.0 else int((x / y) * 10000) / 10000.0

    def simpleAmount(self, field, number):
        series = self.DF[field].groupby(self.DF[self.groupColName]).sum()
        simpleDF = pd.DataFrame(series, columns=[field])
        simpleDF[field] = simpleDF.apply(lambda row: self.division(row[field], number), axis=1)
        simpleDF.reset_index(inplace=True)
        return simpleDF

    def getAvgDraftGpsAmount(self):
        draftGpsAmount = self.netCheckDF['gps_draft_amount'].sum()
        condition = (self.netCheckDF['gps_amount'] > 0) & (self.netCheckDF['gps_amount_his'] > 0)
        vehOnlineCnt = self.netCheckDF[condition].shape[0]  # 行数, 或用len()
        if vehOnlineCnt == 0.0:
            return 0.0
        else:
            return self.division(draftGpsAmount, vehOnlineCnt)

    def veh_net(self):
        series = self.DF[self.DF['gps_amount_his'] > 0] \
            .groupby(self.DF[self.groupColName]) \
            .size()
        vehNetDF = pd.DataFrame(series, columns=['veh_net'])
        vehNetDF.reset_index(inplace=True)
        return vehNetDF

    def veh_online(self):
        series = self.DF[(self.DF['gps_amount'] > 0) & (self.DF['gps_amount_his'] > 0)] \
            .groupby(self.DF[self.groupColName]) \
            .size()
        vehOnlineDF = pd.DataFrame(series, columns=['veh_online'])
        vehOnlineDF.reset_index(inplace=True)
        return vehOnlineDF

    def avg_po_amount(self):
        po_amount_DF = self.simpleAmount('po_amount', 1.0)
        vehOnlineDF = self.veh_online()

        DF2 = pd.merge(po_amount_DF, vehOnlineDF, on=self.groupColName, how='left')
        DF2['avg_po_amount'] = DF2.apply(lambda row: self.division(row['po_amount'], row['veh_online']), axis=1)
        tmpDF = DF2[[self.groupColName, 'avg_po_amount']]
        return tmpDF

    def avg_fd_amount(self):
        fd_amount_DF = self.simpleAmount('fd_amount', 1.0)
        vehOnlineDF = self.veh_online()
        DF2 = pd.merge(fd_amount_DF, vehOnlineDF, on=self.groupColName, how='left')
        DF2['avg_fd_amount'] = DF2.apply(lambda row: self.division(row['fd_amount'], row['veh_online']), axis=1)
        tmpDF = DF2[[self.groupColName, 'avg_fd_amount']]
        return tmpDF

    def avg_bt_amount(self):
        bt_amount_DF = self.simpleAmount('bt_amount', 1.0)
        vehOnlineDF = self.veh_online()
        DF2 = pd.merge(bt_amount_DF, vehOnlineDF, on=self.groupColName, how='left')
        DF2['avg_bt_amount'] = DF2.apply(lambda row: self.division(row['bt_amount'], row['veh_online']), axis=1)
        tmpDF = DF2[[self.groupColName, 'avg_bt_amount']]
        return tmpDF

    def draft_amount(self):
        AvgDraftGpsAmount = self.getAvgDraftGpsAmount()
        condition = (self.DF['gps_draft_amount'] > AvgDraftGpsAmount) & (self.DF['gps_amount_his'] > 0)
        series = self.DF[condition].groupby(self.DF[self.groupColName]).size()
        tmpDF = pd.DataFrame(series, columns=['draft_amount'])
        tmpDF.reset_index(inplace=True)
        return tmpDF

    def draft_rate(self):
        AvgDraftGpsAmount = self.getAvgDraftGpsAmount()
        condition = (self.DF['gps_draft_amount'] > AvgDraftGpsAmount) & (self.DF['gps_amount_his'] > 0)
        series = self.DF[condition].groupby(self.DF[self.groupColName]).size()
        DF1 = pd.DataFrame(series, columns=['draft_amount'])
        DF1.reset_index(inplace=True)
        vehOnlineDF = self.veh_online()
        DF2 = pd.merge(DF1, vehOnlineDF, on=self.groupColName, how='inner')
        DF2['draft_rate'] = DF2.apply(lambda row: self.division(row['draft_amount'], row['veh_online']), axis=1)
        tmpDF = DF2[[self.groupColName, 'draft_rate']]
        return tmpDF

    def gps_amount(self):
        series = self.DF.loc[
            (self.DF['gps_amount'] > 0) & (self.DF['gps_amount_his'] > 0), 'gps_amount'] \
            .groupby(self.DF[self.groupColName]) \
            .sum()
        gpsAmountDF = pd.DataFrame(series, columns=['gps_amount'])
        gpsAmountDF.reset_index(inplace=True)
        return gpsAmountDF

    def gps_total_amount(self):
        series = self.DF.loc[
            (self.DF['gps_total_amount'] > 0) & (self.DF['gps_amount_his'] > 0), 'gps_total_amount'] \
            .groupby(self.DF[self.groupColName]) \
            .sum()
        gpsTotalAmountDF = pd.DataFrame(series, columns=['gps_total_amount'])
        gpsTotalAmountDF.reset_index(inplace=True)
        return gpsTotalAmountDF

    def qualifi_rate(self):
        gpsAmountDF = self.gps_amount()
        gpsTotalAmountDF = self.gps_total_amount()
        DF1 = pd.merge(gpsAmountDF, gpsTotalAmountDF, on=self.groupColName, how='inner')
        DF1['qualifi_rate'] = DF1.apply(lambda row: self.division(row['gps_amount'], row['gps_total_amount']), axis=1)
        tmpDF = DF1[[self.groupColName, 'qualifi_rate']]
        return tmpDF

    def line_rate(self):
        vehOnlineDF = self.veh_online()
        vehNetDF = self.veh_net()
        DF1 = pd.merge(vehOnlineDF, vehNetDF, on=self.groupColName, how='inner')
        DF1['line_rate'] = DF1.apply(lambda row: self.division(row['veh_online'], row['veh_net']), axis=1)
        tmpDF = DF1[[self.groupColName, 'line_rate']]
        return tmpDF

    def mileage_rate(self):
        mileage_DF = self.simpleAmount('mileage', 10.0)
        mileage_total_DF = self.simpleAmount('mileage_total', 10.0)
        DF1 = pd.merge(mileage_DF, mileage_total_DF, on=self.groupColName, how='inner')
        DF1['mileage_rate'] = DF1.apply(lambda row: self.division(row['mileage'], row['mileage_total']), axis=1)
        DF1.reset_index(inplace=True)
        mileageRateDF = DF1[[self.groupColName, 'mileage_rate']]
        return mileageRateDF

    def alarm_ser_rate(self):
        alarm_ser_deal_amount_DF = self.simpleAmount('alarm_ser_deal_amount', 1.0)
        alarm_ser_amount_DF = self.simpleAmount('alarm_ser_amount', 1.0)
        DF1 = pd.merge(alarm_ser_deal_amount_DF, alarm_ser_amount_DF, on=self.groupColName, how='inner')
        DF1['alarm_ser_rate'] = DF1.apply(
            lambda row: self.division(row['alarm_ser_deal_amount'], row['alarm_ser_amount']), axis=1)
        DF1.reset_index(inplace=True)
        alarmSerRateDF = DF1[[self.groupColName, 'alarm_ser_rate']]
        return alarmSerRateDF

    ###### 按city_name分组聚合生成各项指标DF, DF[[self.groupColName+'指标']] #######
    def getQuotaColAggrDFList(self):
        # simple fields AGGR
        po_amount_DF = self.simpleAmount('po_amount', 1.0)
        fd_amount_DF = self.simpleAmount('fd_amount', 1.0)
        bt_amount_DF = self.simpleAmount('bt_amount', 1.0)
        mileage_DF = self.simpleAmount('mileage', 10.0)
        mileage_total_DF = self.simpleAmount('mileage_total', 10.0)
        alarm_ser_deal_amount_DF = self.simpleAmount('alarm_ser_deal_amount', 1.0)
        alarm_ser_amount_DF = self.simpleAmount('alarm_ser_amount', 1.0)

        # complex fields AGGR
        avg_po_amount_DF = self.avg_po_amount()
        avg_fd_amount_DF = self.avg_fd_amount()
        avg_bt_amount_DF = self.avg_bt_amount()
        veh_online_DF = self.veh_online()
        veh_net_DF = self.veh_net()
        draft_amount_DF = self.draft_amount()
        draft_rate_DF = self.draft_rate()
        gps_amount_DF = self.gps_amount()
        gps_total_amount_DF = self.gps_total_amount()
        qualifi_rate_DF = self.qualifi_rate()
        line_rate_DF = self.line_rate()
        mileage_rate_DF = self.mileage_rate()
        alarm_ser_rate_DF = self.alarm_ser_rate()

        # 按组聚合生成的所有指标列
        quotaColAggrDFList = [po_amount_DF, fd_amount_DF, bt_amount_DF, mileage_DF, mileage_total_DF,
                              alarm_ser_deal_amount_DF, alarm_ser_amount_DF, avg_po_amount_DF,
                              avg_fd_amount_DF, avg_bt_amount_DF, veh_online_DF, veh_net_DF, draft_amount_DF,
                              draft_rate_DF,
                              gps_amount_DF, gps_total_amount_DF, qualifi_rate_DF,
                              line_rate_DF, mileage_rate_DF, alarm_ser_rate_DF]

        return quotaColAggrDFList
