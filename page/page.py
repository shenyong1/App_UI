# -*- coding:utf-8 -*-
from lib.appController import driver_queue
from lib.pyapp import Pyapp
from appium.webdriver.common.touch_action import TouchAction

class BasePage(object):
    def __init__(self):
        #通过队列取driver
        self.driver = driver_queue.get()
        #实列化pyapp 并获取pyapp实列对象
        self.pyapp = Pyapp(self.driver)

    def quit(self):
        self.pyapp.quit()

class LoginPage(BasePage):
    def username(self):
        css = 'content=>请输入QQ号码或手机或邮箱'
        self.pyapp.type(css, 136945832)

    def password(self):
        css = 'content=>密码 安全'
        self.pyapp.type(css, 43052719920616)

    def login(self):
        css = 'android=>new UiSelector().text("登 录")'
        self.pyapp.click(css)

    def setting(self):
        css = 'content=>帐户及设置'
        self.pyapp.click(css)

    def setting_1(self):
        css = 'content=>设置'
        self.pyapp.click(css)

    def check_setting2(self):
        css = 'android=>new UiSelector().text("帐号、设备安全")'
        self.pyapp.wait_and_save_exception(css,'error')

    def setting_2(self):
        css = 'android=>new UiSelector().text("帐号、设备安全")'
        self.pyapp.click(css)

    def setting_3(self):
        css = 'content=>手势密码锁定'
        self.pyapp.click(css)

    def setting_4(self):
        css = 'android=>new UiSelector().text("创建手势密码")'
        self.pyapp.click(css)

    def setting_5(self):
        element = self.pyapp.get_elements('class=>android.view.View')[12]
        # 他在整个页面的位置
        location = element.location
        size = element.size
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']
        xxx = width / 6
        one_x = x + xxx
        one_y = y + xxx
        two_x = x + xxx * 3
        two_y = y + xxx
        # TouchAction(local.driver).press(x=onex,y=oney).wait(300).move_to(x=twox-onex,y=twoy-oney).wait(300).move_to(x=threex-twox,y=threey-twoy).wait(300).move_to(x=fourx-threex,y=foury-threey).perform()
        TouchAction(self.driver).press(x=one_x, y=one_y).wait(300).move_to(x=two_x - one_x, y=two_y - one_y).perform()

class Page(LoginPage):
    pass