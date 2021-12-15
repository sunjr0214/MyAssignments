#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys

import pandas as pd
from sqlalchemy import create_engine

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


def getEngine(urlList):
    # 初始化数据库连接，使用pymysql模块
    connUrl = 'mysql+pymysql://%s:%s@%s:%s/%s' % (urlList)
    engine = create_engine(connUrl, connect_args={'charset': 'utf8'})
    return engine


def generateDF(sql, engine):
    # 实现查询：read_sql_query的两个参数: sql语句， 数据库连接
    DF = pd.read_sql_query(sql, engine)
    return DF


def getTmpWhiteistSql():
    tmp_fd_whiteist_sql = 'select * from tmp_fd_whiteist'
    tmp_bt_whiteist_sql = 'select * from tmp_bt_whiteist'

    return tmp_fd_whiteist_sql, tmp_bt_whiteist_sql


def getVehicleExtendMonthSql(endMonthStr, *cityIdList):
    if len(cityIdList) == 0:
        vehicle_extend_month_sql = \
            '''select * from vehicle_extend_month where stat_day = %s and industry in (1,2,4)''' % (endMonthStr)

    else:
        vehicle_extend_month_sql = \
            '''select * from vehicle_extend_month where stat_day = %s and city_id =  '%s' and industry in (1,2,4)''' % (
                endMonthStr, cityIdList[0])
    return vehicle_extend_month_sql


def getNetCheckVehDaySql(startDay, endDay):
    net_check_veh_month_sql = \
        '''select vehicle_id as vehicle_id,
            sum(fd_amount) as fd_amount,
            sum(po_amount) as po_amount,
            sum(bt_amount) as bt_amount,
            sum(mileage) as mileage,
            sum(mileage_total) as mileage_total,
            sum(gps_total_amount) as gps_total_amount,
            sum(gps_amount) as gps_amount,
            sum(gps_draft_amount) as gps_draft_amount,
            sum(gps_amount_his) as gps_amount_his,
            sum(alarm_ser_amount) as alarm_ser_amount,
            sum(alarm_ser_deal_amount) as alarm_ser_deal_amount 
        from net_check_veh_day where stat_day >= %s and stat_day <= %s group by vehicle_id''' % (startDay, endDay)

    return net_check_veh_month_sql


# 城市、运管所、企业、
def getCompanyDimSql(endMonthStr, cityId):
    companyDimSql = \
        '''select city_name,transport_mng_name,company_name from vehicle_extend_month where stat_day = %s and city_id = %s and industry in (1,2,4) group by city_name,transport_mng_name,company_name''' % (
        endMonthStr, cityId)

    return companyDimSql


# 城市、运管所
def getTransportDimSql(endMonthStr, cityId):
    transportDimSql = \
        '''select city_name,transport_mng_name from vehicle_extend_month where stat_day = %s and city_id = %s and industry in (1,2,4) group by city_name,transport_mng_name''' % (
            endMonthStr, cityId)

    return transportDimSql
