# -*- coding:utf-8 -*-
import json,yaml
import sys,os


class Configure(object):
    @property
    def app_data(self):
        with open(APP_DATA_PATH,'rb') as f:
            data = yaml.load(f)

        return data

    @property
    def app_element_data(self):
        with open(ELEMENT_REPORT,'rb') as f:
            data = yaml.load(f)
        return data



BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#手机信息地址
APP_DATA_PATH = os.path.join(BASE_PATH,'conf/appController.yml')

CONF_PATH = os.path.join(BASE_PATH,'conf')

#元素
ELEMENT_REPORT = os.path.join(CONF_PATH,'element_test.yml')

#日志存放地址
LOG_PATH = os.path.join(BASE_PATH,'log')

LOG_NAME = 'appUI.log'

LOG_LEVER = 'debug'
if __name__ == '__main__':
    tt = Configure().app_data
    print(tt)