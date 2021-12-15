#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os


# if sys.getdefaultencoding() != 'utf-8':
#     reload(sys)
#     sys.setdefaultencoding('utf-8')


def getTemplateFilePath(TemplateExcName):
    TemplatePath = os.path.abspath(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "../xlsx/template/" + TemplateExcName))
    return TemplatePath.replace('\\', '/')



def getOneCitySingleMonthReportSavePath(saveExcName):
    savePath = os.path.abspath(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "../xlsx/Reports/OneCitySingleMonth/" + saveExcName))
    return savePath.replace('\\', '/')


def getSingleMonthReportSavePath(saveExcName):
    savePath = os.path.abspath(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "../xlsx/Reports/AllCitySingleMonth/" + saveExcName))
    return savePath.replace('\\', '/')


def getMultiMonthReportSavePath(saveExcName):
    savePath = os.path.abspath(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "../xlsx/Reports/AllCityMultiMonth/" + saveExcName))
    return savePath.replace('\\', '/')


def getPostNetCheckPath(postExcName):
    PostNetCheckPath = os.path.abspath(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "../xlsx/PostNetCheckTab/" + postExcName))
    return PostNetCheckPath.replace('\\', '/')
