#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division

import os
import sys
from ConfigParser import ConfigParser

from dill.dill import FileNotFoundError


# if sys.getdefaultencoding() != 'utf-8':
#     reload(sys)
#     sys.setdefaultencoding('utf-8')


class Config(object):
    def __init__(self):
        self.confFilePath = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),'../conf/config.ini'))
        if not os.path.exists(self.confFilePath):
            raise FileNotFoundError("配置文件不存在")
        self.conf = ConfigParser()
        self.conf.read(self.confFilePath)

    def getConfig(self, section, option):
        return self.conf.get(section, option)

