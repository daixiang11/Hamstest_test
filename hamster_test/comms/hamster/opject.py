import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from hamster_test.comms.constants import ERROR_FILE
from hamster_test.comms.yaml_utils import get_picture
from hamster_test.comms.log_utils import get_logger
from selenium.webdriver import ActionChains

"""
定义Hamster操作指令
"""


class Hamster(object):
    """
    用于封装hamster的操作方法
    """

    def __init__(self, driver):
        self.driver = driver

    def geturl(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            print('打开网页失败')
            get_picture(self.driver, '打开网页失败')  # 失败截图
            get_logger().error(f"打开{url}网页失败")
            allure.attach.file(ERROR_FILE, name='longing error', attachment_type=allure.attachment_type.TEXT)
            raise e

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
            get_logger().error("切换窗口失败")
            allure.attach.file(ERROR_FILE, name='longing error', attachment_type=allure.attachment_type.TEXT)
            raise e

    # 输入框输入内容
    def send_keys(self, time, path, element, value):
        """

        :param time: 定位元素的最大等待时间
        :param path: 元素定位的方法
        :param element: 为需要定位的元素
        :param value: 需要填入的值
        :return:
        """
        try:
            el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((path, element)))
            el.send_keys(value)
        except Exception as e:
            print('输入{}失败'.format(value))
            get_picture(self.driver, r'输入{}失败'.format(value))  # 失败截图
            get_logger().error('元素为' + element + '输入的值为{}失败'.format(value))
            allure.attach.file(ERROR_FILE, name='longing error', attachment_type=allure.attachment_type.TEXT)
            raise e

    # 点击方法
    def click(self, time, path, element):
        """

        :param time: 最大等待时间
        :param path: 元素定位的方法
        :param elment: 定位的元素
        :return:
        """
        try:
            el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((path, element)))
            el.click()
        except Exception as e:
            print(element + '元素点击失败')
            get_picture(self.driver, '元素点击失败')  # 失败截图
            get_logger().error(element + '元素点击失败')
            allure.attach.file(ERROR_FILE, name='longing error', attachment_type=allure.attachment_type.TEXT)
            raise e

    # 当元素可以点击时进行点击
    def clicks(self, time, path, element):
        """

        :param time: 最大等待时间
        :param path: 元素定位的方法
        :param elment: 定位的元素
        :return:
        """
        try:
            el = WebDriverWait(self.driver, time).until(ec.element_to_be_clickable((path, element)))
            el.click()
        except Exception as e:
            print(element + '元素点击失败')
            get_picture(self.driver, '元素点击失败')  # 失败截图
            get_logger().error(element + '元素点击失败')
            allure.attach.file(ERROR_FILE, name='longing error', attachment_type=allure.attachment_type.TEXT)
            raise e

    # 判断元素是否有获取到
    def iselement(self, time, path, element):
        """
        基本实现判断元素是否存在
        :param time: 获取元素对象的最大等待时间
        :param path: 元素定位方法
        :param element: 需要输入的元素
        :return: bool
        """
        try:
            el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((path, element)))
            return True
        except Exception as e:
            return False

    # 获取元素里面的文本信息
    def text(self, time, path, element):
        """

        :param time:获取元素的最大等待时间
        :param path: 元素定位方法
        :param element: 需要输入的元素
        :return: 获取到的文本信息
        """
        try:
            el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((path, element)))
            tx = el.text
            return tx
        except Exception as e:
            print('查询{}文本失败'.format(element))
            get_picture(self.driver, '查询文本失败')  # 失败截图
            get_logger().error('元素为' + element + '查询文本失败')
            allure.attach.file(ERROR_FILE, name='longing error', attachment_type=allure.attachment_type.TEXT)
            raise e

    # 定位到某个元素的位置并且点击
    def target(self, time, path, element):
        """

        :param time:最大等待时间
        :param path: 定位元素的方法
        :param element: 需要输入的元素
        :return:
        """
        try:
            target = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((path, element)))
            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            target.click()
        except Exception as e:
            print('下拉定位{}元素失败'.format(element))
            get_picture(self.driver, '下拉定位元素失败')  # 失败截图
            get_logger().error('下拉定位元素为' + element + '定位失败')
            allure.attach.file(ERROR_FILE, name='longing error', attachment_type=allure.attachment_type.TEXT)
            raise e

    # 将鼠标悬浮在某个元素上
    def move_to_element(self, time, path, element):
        try:
            el = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((path, element)))
            ActionChains(self.driver).move_to_element(el).perform()
        except Exception as e:
            print('鼠标悬浮{}元素失败'.format(element))
            get_picture(self.driver, '鼠标悬浮元素失败')  # 失败截图
            get_logger().error('元素为' + element + '鼠标悬浮该元素失败')
            allure.attach.file(ERROR_FILE, name='longing error', attachment_type=allure.attachment_type.TEXT)
            raise e


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=option)
    o = Hamster(driver)
    driver.get('https://www.baidu.com')
    o.click(3, By.ID, '111')
