from lib.path import LOGPATH, APPPICTUREPATH
from lib.tool import Tool
import os,time
import subprocess
from lib.log import logger
from appium import webdriver
import queue,threading

#实例化队列 python自带的队列
#存放driver的队列
driver_queue = queue.Queue()

#多线程隔离
local = threading.local()

#存放手机设备名称的对列，用于区分线程
device_name_queue = queue.Queue()






class AppController(object):
    def __init__(self):
        self.tool = Tool()
        #获取所有配置信息
        self.yml = self.tool.app_data
        #操作系统
        self.device_type = self.yml.get('device_type')
        #测试APP信息
        self.tester = self.yml.get('tester')
        #获取所有手机配置信息
        self.devices = self.yml.get('devices')
        #设备名称
        self.deviceName = self.devices.get(self.device_type)[0].get('deviceName')
        #用于校验服务是否成功，存放端口号
        self.ports = []


    def kill_server(self):
        """
        adb如果重启  夜游神将不会被查到
        :return:
        """
        logger.debug('执行[KiLL SERVER]操作:%s'%subprocess.getoutput("taskkill /F /IM node.exe /t"))
        logger.debug('重启ADB服务！%s'%subprocess.getoutput("adb kill-server"))


    #启动appium服务
    def start_server(self):
        self.kill_server()
        threads_server = []
        #获取一个手机的信息
        device = self.devices.get(self.device_type)[0]
        #添加端口号 为校验服务是否启动成功做准备
        self.ports.append(device.get('port'))
        #拼接日志路径
        log_path = os.path.join(LOGPATH,device.get('name')+'.log')
        #拼接启动命令
        command = 'appium -a {ip} -p {port} -U {deviceName} -g {log}'.format(ip=device.get('ip'),
                                                                             port=device.get('port'),
                                                                             deviceName=device.get(
                                                                                 'deviceName'),
                                                                             log=log_path)
        logger.debug('启动服务的命令：%s'%command)
        #多进程的方式执行命令
        subprocess.Popen(command, stdout=open(log_path, 'a+'), stderr=subprocess.PIPE, shell=True)

    def test_sever(self):
        # 通过命令 一遍一遍的查找 如果有返回值则代表成功启动 没有返回值代表启动失败
        #netstat - ano | findstr 4723

        while True:
            s = subprocess.getoutput('netstat -ano | findstr %s'%self.ports[0])
            if s:
                logger.debug('端口：【%s】 启动成功'%self.ports[0])
                break
            else:
                logger.debug('端口：【%s】 启动失败  5秒后重试'%self.ports[0])
                time.sleep(5)
        return True

    #启动driver
    def start_driver(self):
        #首先要拿到初始化app的信息，也就是tester
        # 还要拿到手机信息
        # 最后拼我们的url 和参数
        # 获取手机信息
        device = self.devices.get(self.device_type)[0]
        #合并手机信息与tester信息
        self.tester.update(device)
        # print(self.tester)
        driver = webdriver.Remote('http://{ip}:{port}/wd/hub'.format(port=device.get('port'),
                                                 ip=device.get('ip')),self.tester)
        #将创建好的driver添加到队列中
        driver_queue.put(driver)



if __name__ == '__main__':
    d = AppController()
    d.start_server()
    d.test_sever()
    d.start_driver()
