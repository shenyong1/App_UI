import json
import os
from lib.path import WEBPICTUREPATH, APPPICTUREPATH, APPERROR,APPPATH,APPPICTURE
from lib.log import logger
import yaml


class Tool(object):
    @property
    def app_data(self):
        with open(APPPATH, 'rb') as f:
            data = yaml.load(f)
        return data

    def app_error_picture(self):
        app_list = os.listdir(APPPICTURE)
        app_picture = []
        for item in app_list:
            if item.endswith('.jpg'):
                app_picture.append((APPERROR + item,))
        return app_picture

    @staticmethod
    def app_clear():
        app_list = os.listdir(APPPICTURE)
        logger.debug('上次执行的未删除的图片：%s' % app_list)
        for p in app_list:
            if p.endswith('jpg') or p.endswith('png'):
                os.remove(os.path.join(APPPICTURE, p))
