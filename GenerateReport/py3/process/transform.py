#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division

import sys

import pandas as pd


# if sys.getdefaultencoding() != 'utf-8':
#     reload(sys)
#     sys.setdefaultencoding('utf-8')


# 过滤白名单车辆
def filterWhite(vehExDF, netCheckDF, *whDF):
    fdWtDF, btWtDF = whDF
    # 拼接where条件字段
    fdWtDF['car_license_color'] = fdWtDF['car_license'] + '_' + fdWtDF['color'].map(str)
    btWtDF['car_license_color'] = btWtDF['car_license'] + '_' + btWtDF['color'].map(str)
    vehExDF['car_license_color'] = vehExDF['car_license'] + '_' + vehExDF['plate_color'].map(str)
    # 表关联
    vehExWtDF1 = pd.merge(vehExDF, fdWtDF, on='car_license_color', how='inner')
    vehExWtDF2 = pd.merge(vehExDF, btWtDF, on='car_license_color', how='inner')

    # fd_amount字段值置为0
    vehExWt1 = vehExWtDF1['vehicle_id'].values.tolist()
    vehExWt2 = vehExWtDF2['vehicle_id'].values.tolist()
    netCheckDF.loc[netCheckDF['vehicle_id'].isin(vehExWt1), 'fd_amount'] = 0
    netCheckDF.loc[netCheckDF['vehicle_id'].isin(vehExWt2), 'bt_amount'] = 0

    # 恢复索引
    fdWtDF.reset_index(inplace=True)
    btWtDF.reset_index(inplace=True)
    vehExDF.reset_index(inplace=True)

    return netCheckDF

