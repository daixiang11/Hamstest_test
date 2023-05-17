import time

import pytest
from selenium import webdriver
from hamster_test.comms.yaml_utils import get_ini_data, get_picture

import allure


@pytest.fixture()
def connect_db():
    option = webdriver.ChromeOptions()
    option.add_argument("--user-data-dir=" + get_ini_data('version', 'chrome_Default'))  # 添加获取到的配置文件路径
    option.add_experimental_option('detach', True)  # 浏览器不会自动关闭
    driver = webdriver.Chrome(chrome_options=option, options=option)  # 打开配置插件的chrome浏览器
    driver.maximize_window()  # 浏览器窗口最大化
    yield driver
    driver.quit()  # 关闭浏览器


@pytest.fixture(scope='function')
def connect_db1():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=option)
    # option = webdriver.ChromeOptions()
    # option.add_experimental_option('detach', True)  # 浏览器不会自动关闭
    # driver = webdriver.Chrome(chrome_options=option, options=option)  # 打开配置插件的chrome浏览器
    driver.maximize_window()  # 浏览器窗口最大化
    yield driver
    driver.quit()  # 关闭浏览器


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的name和nodeid的中文显示在控制台上
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        print(i.nodeid)
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")


# 以上代码的作用是将当前目录下的默认编码unicode更改为utf-8的编码格式这样更加有利于中文的展示




