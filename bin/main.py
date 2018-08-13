# -*- coding:utf-8 -*-

from lib.appController import AppController
import unittest
from lib.path import APPCASEPATH,APPREPORT
from lib.HTMLTestAppRunner import HTMLTestRunner
class Main(object):
    def __init__(self):
        self.controller = AppController()
        self.deviceName = self.controller.deviceName

    def run(self):
        #启动服务
        self.controller.start_server()
        #校验服务
        if self.controller.test_sever():
            self.controller.start_driver()
            suit = unittest.TestSuite()
            cases = unittest.defaultTestLoader.discover(APPCASEPATH)
            for case in cases:
                suit.addTest(case)

            f = open(APPREPORT.format('{}.html'.format(self.deviceName)), 'wb')
            runner = HTMLTestRunner(f, verbosity=1, title=u'测试报告', description=u'用例执行情况：')
            runner.run(suit)
            f.flush()
            f.close()





if __name__ == '__main__':
    Main().run()