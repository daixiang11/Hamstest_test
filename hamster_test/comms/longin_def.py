import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from hamster_test.comms.yaml_utils import get_picture
from hamster_test.test_cases.test_contract.test_contract_evm import logger
from selenium.common import exceptions


# 封装一个页面操作的总类
class Login:
    """
    该类封装的方法为登录页面的方法

    """

    # 重构ini方法打开浏览器
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # 登录网址
    def geturl(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            print('打开网页失败')
            get_picture(self.driver, '打开网页失败')  # 失败截图
            logger.error(f"打开{url}网页失败")
            # raise e

    # 切换浏览器的窗口
    def window(self, int):
        """

        :param int: 切换网页的窗口号
        :return:
        """
        try:
            self.driver.switch_to.window(self.driver.window_handles[int])
        except Exception as e:
            print('窗口切换失败')
            get_picture(self.driver, '窗口切换失败')  # 失败截图
            logger.error("切换窗口失败")
            raise e

    # 输入框输入内容
    def send_keys(self, time, element, value, xpath=None):
        """

        :param time: 定位元素的最大等待时间
        :param element: 为需要定位的元素
        :param value: 需要填入的值
        :param xpath: 为定位元素的方法，默认为xpath
        :return:
        """
        try:
            if xpath is None:
                el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.XPATH, element)))
                el.send_keys(value)
            if xpath == 'name':
                el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.NAME, element)))
                el.send_keys(value)
            if xpath == 'class':
                el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.CLASS_NAME, element)))
                el.send_keys(value)
            if xpath == 'id':
                el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.ID, element)))
                el.send_keys(value)
            if xpath == 'text':
                el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.LINK_TEXT, element)))
                el.send_keys(value)
        except Exception as e:
            print('输入{}失败'.format(value))
            get_picture(self.driver, '输入{}失败'.format(value))  # 失败截图
            logger.error('元素为' + element + '输入的值为{}失败'.format(value))
            raise e

    # 点击点击按钮
    def click(self, time, element, xpath=None):
        """

        :param time: time定位元素的最大等待时间
        :param element: element，为需要定位的元素
        :param xpath: xpath为定位元素的方法，默认为xpath
        :return:
        """
        try:
            if xpath is None:
                el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.XPATH, element)))
                el.click()
            if xpath == 'class':
                el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.CLASS_NAME, element)))
                el.click()
            if xpath == 'id':
                el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.ID, element)))
                el.click()
            if xpath == 'text':
                el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.LINK_TEXT, element)))
                el.click()
            if xpath == 'name':
                el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.NAME, element)))
                el.click()
        except Exception as e:
            print(element + '元素点击失败')
            get_picture(self.driver, element + '元素点击失败')  # 失败截图
            logger.error(element + '元素点击失败')
            raise e

    # 判断元素是否存在
    def iselement(self, time, element, xpaths=None):
        """
        基本实现判断元素是否存在
        :param time: 获取元素对象的最大等待时间
        :param element: 需要输入的元素
        :param xpaths: xpaths表达式
        :return: bool
        """
        try:
            if xpaths is None:
                el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.XPATH, element)))
                return True
            if xpaths == "id":
                self.driver.find_element(By.ID, element)
                return True
            if xpaths == 'name':
                self.driver.find_element(By.NAME, element)
                return True
            if xpaths == "class":
                self.driver.find_element(By.CLASS_NAME, element)
                return True
        except Exception as e:
            return False

    # 获取当前页面的URL地址
    def current_url(self):
        url = self.driver.current_url
        return url

    # 获取当前页面的文本信息
    def text(self, time, element, xpath=None):
        """

        :param time:获取元素的最大等待时间
        :param element: 需要输入的元素
        :param xpath: 属性方法默认为xpath
        :return: 获取到的文本信息
        """
        try:
            if xpath is None:
                el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.XPATH, element)))
                tx = el.text
                return tx
            if xpath == 'id':
                el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.ID, element)))
                tx = el.text
                return tx
            if xpath == 'name':
                el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.NAME, element)))
                tx = el.text
                return tx
            if xpath == 'class':
                el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.CLASS_NAME, element)))
                tx = el.text
                return tx
        except Exception as e:
            print('查询{}文本失败'.format(element))
            get_picture(self.driver, '查询{}文本失败'.format(element))  # 失败截图
            logger.error('元素为' + element + '查询文本失败')
            raise e

    # 对当前的页面进行截图
    def picture(self, file):
        """

        :param file:截图需要的文件名
        :return:
        """
        get_picture(self.driver, '查询{}文本失败'.format(file))  # 失败截图


if __name__ == '__main__':
    hm = Login()
    hm.geturl("https://develop.alpha.hamsternet.io/projects")
    a = hm.iselement(5, '//*[@id="js-oauth-authorize-btn"]')
    print(a)
    if hm.iselement(5, '//*[@id="js-oauth-authorize-btn"]'):
        hm.click(5, '//*[@id="js-oauth-authorize-btn"]')

    hm.click(5, "//*[@id='app']/div/div[2]/div[2]/span")
    hm.window(-1)
    hm.send_keys(5, 'login', '983643937@qq.com', 'name')
    hm.send_keys(5, 'password', 'Dx3826729', 'name')

    hm.click(10, 'commit', 'name')
    hm.window(0)
    if hm.iselement(5, '//*[@id="js-oauth-authorize-btn"]'):
        hm.click(5, '//*[@id="js-oauth-authorize-btn"]')
    # hm.window(0)
    if hm.iselement(5, '//*[@id="layout-default"]/section/main/div[1]/div[1]/button'):
        hm.click(5, '//*[@id="layout-default"]/section/main/div[1]/div[1]/button')
    time.sleep(30)
