# -*- coding:utf-8 -*-
#date:  2018/7/5
from lib.pyapp import Pyapp
import threading
from lib.log import logger

from lib.getElement import GetElement

local = threading.local()

class ComTools(object):
    def __init__(self,driver=None):
        if driver:
            local.driver = driver
            local.pyapp = Pyapp(local.driver)
        else:
            pass

    def click(self,name):
        e = GetElement().get_element_name(name)
        local.pyapp.click(e)
        logger.info('点击"'+name+'"成功')