from lib.core.config import Configure
from lib.log import logger

class GetElement(object):
    def __init__(self):
        self.yml = Configure().app_element_data

    def get_element_name(self, name):

        try:

            ele = self.yml.get(name)

            return ele
        except Exception as e:
            logger.info('获取配置文件：element_mijia_bedlight.yml中属性失败！！！')
