import allure
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from hamster_test.comms.constants import DATA_YAML, REPORT_JSON, REPORT_HTML
from hamster_test.comms.is_element import iselement
from hamster_test.comms.log_utils import get_logger
from hamster_test.comms.longin_def import Login
from hamster_test.comms.yaml_utils import get_yaml_data, get_picture, get_ini_data


@allure.epic('hamster系统')
@allure.feature("Contract项目")
@allure.parent_suite('Contract项目')
class TestLongin:
    cases = get_yaml_data(DATA_YAML)  # 读取yaml文件中的测试数据

    @allure.suite("登录模块")
    @allure.description("登录模块")
    @pytest.mark.parametrize('case', cases)
    def test_search(self, case):
        allure.dynamic.title(case['case_title'])
        allure.attach(body=case['url'], name='请求路径')
        # 获取登录对象
        hm = Login()
        # 登录项目网址
        hm.geturl("https://hamsternet.io")
        # 点击登录页面
        hm.click(5, '//*[@id="__nuxt"]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/button')
        # 点击github登录
        hm.click(5, "//*[@id='app']/div/div[2]/div[2]/span")
        # 切换至github页面
        hm.window(-1)
        # 输入登录邮箱
        hm.send_keys(5, 'login', '983643937@qq.com', 'name')
        # 输入邮箱密码
        hm.send_keys(5, 'password', 'Dx3826729', 'name')
        # 点击登录
        hm.click(10, 'commit', 'name')
        # 判断是否需要授权
        time.sleep(3)
        if hm.iselement(5, '//*[@id="js-oauth-authorize-btn"]'):
            hm.click(5, '//*[@id="js-oauth-authorize-btn"]')
        hm.window(0)
        # 判断是否在首页，点击返回首页
        if hm.iselement(5, '//*[@id="layout-default"]/section/main/div[1]/div[1]/button'):
            hm.click(5, '//*[@id="layout-default"]/section/main/div[1]/div[1]/button')
        # 获取最新的项目地址
        new_url = hm.current_url()
        # 获取首页的文本信息
        text = hm.text(5, '//*[@id="layout-default"]/section/main/div/div[2]/div[1]/div')
        logger = get_logger()

        try:
            assert case['new_url'] in new_url  # 断言URL存在搜索内容
            assert case['text']['tx1'] in text and case['text']['tx2'] in text  # 断言搜索后没有出现报错
            # 断言是否有创建项目的按钮
            logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title']))
        except AssertionError as e:
            hm.picture(case['case_title'])
            logger.error("测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'], e))
            logger.exception(e)
            raise e


if __name__ == '__main__':
    pytest.main([__file__])
