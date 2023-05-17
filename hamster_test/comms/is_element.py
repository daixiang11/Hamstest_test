from selenium.common import exceptions
from selenium.webdriver.common.by import By


# 通过xpath方法判断元素是否存在
def iselement(browser, xpaths):
    """
    基本实现判断元素是否存在
    :param browser: 浏览器对象
    :param xpaths: xpaths表达式
    :return: 是否存在
    """
    try:
        browser.find_element(By.XPATH, xpaths)
        return True
    except exceptions.NoSuchElementException:
        return False


def idelement(driver, id):
    """
        基本实现判断元素是否存在
        :param driver: 浏览器对象
        :param id: xpaths表达式
        :return: 是否存在
        """
    try:
        driver.find_element(By.ID, id)
        return True
    except exceptions.NoSuchElementException:
        return False


def csselement(driver, css):
    """
            基本实现判断元素是否存在
            :param css:
            :param driver: 浏览器对象
            :param css: css元素表达式
            :return: 是否存在
            """
    try:
        driver.find_element(By.CSS_SELECTOR, css)
        return True
    except exceptions.NoSuchElementException:
        return False
