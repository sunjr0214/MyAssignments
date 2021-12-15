#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division

import os
import sys

currentPath = os.path.dirname(os.path.realpath(__file__))
py3Path = os.path.abspath(os.path.join(currentPath, '..'))
sys.path.append(py3Path)
from py3.process import config
from py3.process import save2Excel as s2e
from py3.process import tabProcess as tp
from py3.utils import Time as formTim
from py3.process import dao

# if sys.getdefaultencoding() != 'utf-8':
#     reload(sys)
#     sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
    print('''
            ######################################################
            #    Report   Generation    Application    Running   #
            ######################################################
        ''')
    # --------------------------------------读取配置-------------------------------------------
    conf = config.Config()
    # 数据库连接配置
    urlList = eval(conf.getConfig('RDBMSconn', 'urlList'))
    # first Cell Location to save value
    firstCellLoc = eval(conf.getConfig('RiskRankAllCitySingleMonth', 'firstCellLoc'))
    # 统计数据的时间范围
    statDayRange = eval(conf.getConfig('RiskRankAllCitySingleMonth', 'statDayRange'))
    # excel 表头配置
    ExcelTiTleCode1 = eval(conf.getConfig('RiskRankAllCitySingleMonth', 'ExcelTiTleCode1'))
    ExcelTiTleCode2 = eval(conf.getConfig('RiskRankAllCitySingleMonth', 'ExcelTiTleCode2'))

    print('正在生成单月区域风险城市排名报表，请稍后...')

    # 日期预处理
    startDay = str(statDayRange[0])  # yyyymmdd
    endDay = str(statDayRange[1])
    endMonthStr = formTim.getMonthStr(endDay)  # yyyymm
    # 转化时间字符串格式,yyyy年mm月dd日
    startFormDateStr, endFormDateStr = formTim.getFormatedTimeStr(startDay, endDay)

    # -------------------------------------------sql拼接-----------------------------------------------------

    tmp_fd_whiteist_sql, tmp_bt_whiteist_sql = dao.getTmpWhiteistSql()
    vehicle_extend_month_sql = dao.getVehicleExtendMonthSql(endMonthStr)
    net_check_veh_day_sql = dao.getNetCheckVehDaySql(startDay, endDay)

    # -------------------------------------conn database------------------------------------
    # 连接数据库，获取DF
    mysqlEngine = dao.getEngine(urlList)
    fdWtDF = dao.generateDF(tmp_fd_whiteist_sql, mysqlEngine)
    btWtDF = dao.generateDF(tmp_bt_whiteist_sql, mysqlEngine)
    netCheckDF = dao.generateDF(net_check_veh_day_sql, mysqlEngine)
    vehExDF = dao.generateDF(vehicle_extend_month_sql, mysqlEngine)
    # 判空
    if vehExDF.shape[0] == 0 or netCheckDF.shape[0] == 0:
        print('vehicle_extend_month表长：' + str(vehExDF.shape[0]) + '\n')
        print('当前月net_check_veh_day表长：' + str(netCheckDF.shape[0]) + '\n')
        print('存在空表！！！')
        exit(1)

    # -------------------------------------指定分组字段--------------------------------------
    groupColName = 'city_name'

    # -------------------------------------预处理netCheck--------------------------------------

    vehLinkedDF, netCheckDF = tp.preparedOriginTabDF(vehExDF, netCheckDF, fdWtDF, btWtDF, groupColName)

    # --------------------------------------有夜间禁行------------------------------------------
    # 生成大表
    riskRankBigTab1 = tp.generateRiskRank(vehLinkedDF, netCheckDF, groupColName, 0, 1)  # 1表示统计夜间禁行
    # print(riskRankBigTab1)

    # 存储数据
    TemplateExcPrefix = 'Jiangsu_RiskRank_AllCity'
    saveExcPrefix = 'Jiangsu_RiskRank_AllCity_%s-%s' % (startDay, endDay)
    # Excel主题行（大标题）
    theme = '“两客一危”道路运输主动安全重点指标排名表（%s - %s）' % (startFormDateStr, endFormDateStr)
    # savePath格式: {filename}_{统计数据的时间区域}_{报表的生成时间}.xlsx
    savePath = s2e.saveSingleMonthData(TemplateExcPrefix, saveExcPrefix, riskRankBigTab1, ExcelTiTleCode1, firstCellLoc,
                                       theme)
    print('单月区域风险城市排名报表生成完毕，保存路径：%s' % (savePath))

    # ---------------------------------------无夜间禁行---------------------------------------
    # 生成大表
    riskRankBigTab2 = tp.generateRiskRank(vehLinkedDF, netCheckDF, groupColName, 0, 0)  # 0表示不统计夜间禁行

    # 存储数据
    TemplateExcPrefix = 'Jiangsu_RiskRank_AllCity_rm_bt'
    saveExcPrefix = 'Jiangsu_RiskRank_AllCity_rm_bt_%s-%s' % (startDay, endDay)
    theme = '“两客一危”道路运输主动安全重点指标排名表（无夜间禁行）（%s - %s）' % (startFormDateStr, endFormDateStr)
    savePath = s2e.saveSingleMonthData(TemplateExcPrefix, saveExcPrefix, riskRankBigTab2, ExcelTiTleCode2, firstCellLoc,
                                       theme)
    print('单月区域风险城市排名报表（无夜间禁行）生成完毕，保存路径：%s' % (savePath))
