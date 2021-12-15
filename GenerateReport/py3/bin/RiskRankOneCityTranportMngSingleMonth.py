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
from py3.constant import commonConst as coco

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
    # 统计指定城市
    cityName = conf.getConfig('RiskRankOneCitySingleMonth', 'cityName')
    # first Cell Location to save value
    firstCellLoc = eval(conf.getConfig('RiskRankOneCitySingleMonth', 'firstCellLoc'))
    # 统计数据的时间范围
    statDayRange = eval(conf.getConfig('RiskRankOneCitySingleMonth', 'statDayRange'))
    # excel 表头配置
    ExcelTiTleCode2 = eval(conf.getConfig('RiskRankOneCitySingleMonth', 'ExcelTiTleCode2'))

    print('正在生成 %s 区域运管所风险排名报表，请稍后...' % (cityName))

    # 日期预处理
    startDay = str(statDayRange[0])  # yyyymmdd
    endDay = str(statDayRange[1])
    endMonthStr = formTim.getMonthStr(endDay)  # yyyymm

    # -------------------------------------------sql拼接-----------------------------------------------------
    # 获取city_id
    constObj = coco.colNameConst()
    cityName2IdMap = constObj.getCityName2IdMap()
    cityId = cityName2IdMap[cityName]
    #获取拼音
    cityId2NameMap = constObj.getCityId2NameMap()
    cityName = cityId2NameMap[cityId]


    tmp_fd_whiteist_sql, tmp_bt_whiteist_sql = dao.getTmpWhiteistSql()
    vehicle_extend_month_sql = dao.getVehicleExtendMonthSql(endMonthStr, cityId)
    net_check_veh_day_sql = dao.getNetCheckVehDaySql(startDay, endDay)

    # 维表：城市、运管所
    transportDimSql = dao.getTransportDimSql(endMonthStr, cityId)

    # -------------------------------------conn database------------------------------------
    # 连接数据库，获取DF
    mysqlEngine = dao.getEngine(urlList)
    fdWtDF = dao.generateDF(tmp_fd_whiteist_sql, mysqlEngine)
    btWtDF = dao.generateDF(tmp_bt_whiteist_sql, mysqlEngine)
    netCheckDF = dao.generateDF(net_check_veh_day_sql, mysqlEngine)
    vehExDF = dao.generateDF(vehicle_extend_month_sql, mysqlEngine)
    transportDimDF = dao.generateDF(transportDimSql, mysqlEngine)

    # 判空
    if vehExDF.shape[0] == 0 or netCheckDF.shape[0] == 0:
        print('vehicle_extend_month表长：' + str(vehExDF.shape[0]) + '\n')
        print('当前月net_check_veh_day表长：' + str(netCheckDF.shape[0]) + '\n')
        print('存在空表！！！')
        exit(1)
    # -------------------------------------指定分组字段--------------------------------------
    groupColName = 'transport_mng_name'

    # -------------------------------------预处理netCheck--------------------------------------

    vehLinkedDF, netCheckDF = tp.preparedOriginTabDF(vehExDF, netCheckDF, fdWtDF, btWtDF, groupColName)

    # ---------------------------------------区域运管所风险排名，有夜间禁行---------------------------------------
    # 生成大表
    riskRankBigTab = tp.generateRiskRank(vehLinkedDF, netCheckDF, groupColName, transportDimDF, 1)  # 0表示不统计夜间禁行

    # 存储数据
    TemplateExcPrefix = 'Jiangsu_RiskRank_OneCity_TransportMng'
    saveExcPrefix = 'Jiangsu_RiskRank_%s_TransportMng_%s-%s' % (cityName, startDay, endDay)
    # savePath格式: Jiangsu_RiskRank_{cityName}_TransportMng_SingleMonth_{统计数据时间区域}_{报表的生成时间}.xlsx
    savePath = s2e.saveOneCitySingleMonthData(TemplateExcPrefix, saveExcPrefix, riskRankBigTab, ExcelTiTleCode2,
                                              firstCellLoc)
    print('%s 区域运管所风险排名报表生成完毕，保存路径：%s' % (cityName, savePath))
