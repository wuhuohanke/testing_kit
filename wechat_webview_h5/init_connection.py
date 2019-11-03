# coding = utf-8
from appium import webdriver
import subprocess
import os


def start_appium_server():
    os.system('chmod -R 777 ./server_start.sh')
    subprocess.Popen('./server_start.sh')


def kill_appium_server():
    os.system('chmod -R 777 ./server_kill.sh')
    subprocess.Popen('./server_kill.sh')


def set_up():

    """
    {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "CLB0218402007439",
    "appPackage": "com.tencent.mm",
    "appActivity": "com.tencent.mm.ui.LauncherUI",
    "noReset": "True"
    }
    """

    # 连接参数。写死参数为P20个人机器，访问微信app
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = 'CLB0218402007439'
    desired_caps['appPackage'] = 'com.tencent.mm'
    desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
    # noReset：如应用已存在，不重新安装应用
    desired_caps['noReset'] = True
    desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}

    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
    return driver
