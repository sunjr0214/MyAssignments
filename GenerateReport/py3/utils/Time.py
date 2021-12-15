#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import time


def getFormatedTimeStr(startDate,endDate):
    startDateStr = str(startDate)
    endDateStr = str(endDate)

    #转化时间字符串格式
    startDateArray = time.strptime(startDateStr, "%Y%m%d")
    endDateArray = time.strptime(endDateStr, "%Y%m%d")
    startFormDateStr = time.strftime('%Y年%m月%d日', startDateArray)
    endFormDateStr = time.strftime('%Y年%m月%d日', endDateArray)

    return startFormDateStr,endFormDateStr


def getMonthStr(date):
    dateStr = str(date)
    # 转化时间字符串格式
    dateArray = time.strptime(dateStr, "%Y%m%d")
    MonthStr = time.strftime('%Y%m', dateArray)

    return MonthStr

def getLastMonthStr(date):
    dateArray = datetime.datetime.strptime(str(date), "%Y%m%d")
    thisMonthStartDayArray = dateArray.replace(day=1)
    lastMonthEndDayArray = thisMonthStartDayArray + datetime.timedelta(days=-1)
    lastMonth = lastMonthEndDayArray.strftime('%Y%m')

    return lastMonth


def getStartDay(date):
    dateArray = datetime.datetime.strptime(str(date), "%Y%m%d")
    startDayArray = dateArray.replace(day=1)
    startDay = startDayArray.strftime('%Y%m%d')

    return startDay