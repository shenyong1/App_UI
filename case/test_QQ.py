# -*- coding:utf-8 -*-
import unittest
from page.page import Page


class QQDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = Page()

    @classmethod
    def tearDownClass(cls):
        # cls.page.quit()
        pass

    def test_a_url(self):
        # self.page.login()
        self.page.username()
        self.page.password()
        self.page.login()

        self.page.setting()
        self.page.setting_1()
        self.page.check_setting2()
        self.page.setting_2()
        self.page.setting_3()
        self.page.setting_4()
        self.page.setting_5()
