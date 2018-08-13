import os

BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 报告地址
REPORTPATH = BASEPATH + os.path.sep + 'report'

# UI自动化报告地址
WEBREPORT = REPORTPATH + os.path.sep + 'web' + os.path.sep + 'report.html'

# app自动化报告地址
APPREPORT = os.path.join(REPORTPATH, '{}')

# UI自动化报错图片路径
WEBPICTUREPATH = REPORTPATH + os.path.sep + 'web_picture' + os.path.sep

# APP错误图片地址
APPPICTUREPATH = REPORTPATH + os.path.sep + 'app_picture' + os.path.sep

APPPICTURE= REPORTPATH + os.path.sep + 'app_picture' + os.path.sep

# 生成报告时的地址
APPERROR = '../app_picture/{}/'

LOGPATH = BASEPATH + os.path.sep + 'log' + os.path.sep

WEBLOGPATH = LOGPATH + 'server.log'

# appcase path
APPCASEPATH = BASEPATH + os.path.sep + 'case'

CONFPATH = BASEPATH + os.path.sep + 'conf' + os.path.sep

WEBPATH = CONFPATH + 'conf.json'

APPPATH = CONFPATH + 'appController.yml'

ELEMENTPROPERTIES = CONFPATH + 'element_mijia_bedlight.yml'
