import os
import allure
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from hamster_test.comms.constants import DATA_IPFS
from hamster_test.comms.is_element import iselement, idelement, csselement
from hamster_test.comms.log_utils import get_logger
from hamster_test.comms.yaml_utils import get_yaml_data, get_picture, get_ini_data
from hamster_test.comms.hamster.page.create_project import CreateProject
from hamster_test.comms.hamster.elenium import elenium as em

logger = get_logger()


@allure.epic('hamster系统')
@allure.feature("FrontEnd项目合约")
@allure.parent_suite('FrontEnd项目合约')
class TestFrontEnd:
    @pytest.fixture(autouse=True)
    def connect_db(self):
        option = webdriver.ChromeOptions()
        option.add_argument(
            "--user-data-dir=" + get_ini_data('version', 'chrome_Default'))  # 添加获取到的配置文件路径
        option.add_experimental_option('detach', True)  # 浏览器不会自动关闭
        self.driver = webdriver.Chrome(chrome_options=option, options=option)  # 打开配置插件的chrome浏览器
        self.driver.maximize_window()  # 浏览器窗口最大化
        yield
        self.driver.quit()  # 关闭浏览器

    cases = get_yaml_data(os.path.join(DATA_IPFS, 'hamster_create.yaml'))  # 读取yaml文件中的测试数据
    ids = ['测试{}'.format(case['case_title']) for case in cases]

    @allure.suite('IPFS生态创建合约')
    @allure.description("IPFS生态创建合约")
    @pytest.mark.parametrize('case', cases, ids=ids)
    def test_create(self, case):
        allure.dynamic.title(case['case_title'])
        allure.attach(body=case['url'], name='请求路径')
        cp = CreateProject(self.driver)
        # 登录项目网址
        cp.geturl(case['url'])
        # 登录项目
        cp.longin(get_ini_data('github', 'user'), get_ini_data('github', 'passwd'))
        # 打开ipfs合约的展示页面
        cp.open_frontend_ipfs()
        # 点击对应的合约
        cp.click(10, *em.frontend_ipfs[case['case_id'] - 1])
        # 查看view中的前端模板，并获取里面的文本信息
        tx1 = cp.get_frontend_view(*em.create_frontend_view, case['case_id'])
        print(tx1)
        time.sleep(300)
        # 创建前端项目并命名
        cp.create_by_template(case['case_data'])
        # 返回到project页面
        cp.click(30, *em.back_to_project)
        self.driver.refresh()
        # 获取文本和URL地址
        tx2 = cp.text(10, *em.project_frontend_names[0])
        url = self.driver.current_url
        try:
            assert case['new_url'] in url  # 断言URL地址与预期一致
            assert case['text'] in tx1  # 断言文本信息是都存在
            assert case['case_data'] in tx2
            logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title']))
        except AssertionError as e:
            get_picture(self.driver, case['case_title'])  # 失败截图
            logger.error(
                "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'], e))
            logger.exception(e)
            raise e
    #
    # cases1 = get_yaml_data(os.path.join(DATA_IPFS, 'hamster_check.yaml'))  # 读取yaml文件中的测试数据
    # ids1 = ['测试{}'.format(case['case_title']) for case in cases1]
    #
    # @allure.suite('IPFS生态检查合约')
    # @allure.description("IPFS生态检查合约")
    # @pytest.mark.parametrize('case', cases1, ids=ids1)
    # def test_check(self, case):
    #     allure.dynamic.title(case['case_title'])
    #     allure.attach(body=case['url'], name='请求路径')
    #     self.driver.get(case['url'])  # 输入项目地址
    #     time.sleep(3)
    #     # 点击检查按钮
    #     self.driver.find_element(By.XPATH, case['element']['em1']).click()
    #     time.sleep(1)
    #     self.driver.refresh()  # 刷新网页
    #     time.sleep(3)
    #     # 判断代码是否检查成功
    #     tm = 0
    #     while tm < 100:
    #         time.sleep(3)
    #         tx = self.driver.find_element(By.XPATH, case['element']['em2']).text
    #         if 'Success' not in tx:
    #             time.sleep(3)
    #         else:
    #             break
    #         tm += 1
    #     time.sleep(3)
    #     self.driver.refresh()
    #     # 点击检查的详情页面
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, case['element']['em3']).click()
    #     time.sleep(3)
    #     # 获取页面的文本信息
    #     tx1 = self.driver.find_element(By.XPATH, case['element']['em4']).text
    #     time.sleep(3)
    #     tx2 = self.driver.find_element(By.XPATH, case['element']['em5']).text
    #     new_url = self.driver.current_url
    #     self.driver.find_element(By.XPATH, case['element']['em6']).click()
    #     time.sleep(3)
    #     print(tx1, tx2)
    #     try:
    #         assert case['text']['tx1'] in tx1
    #         assert case['text']['tx2'] in tx2
    #         assert case['new_url'] in new_url
    #         logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title']))
    #     except AssertionError as e:
    #         get_picture(self.driver, case['case_title'])  # 失败截图
    #         logger.error(
    #             "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'], e))
    #         logger.exception(e)
    #         raise e
    #
    # cases2 = get_yaml_data(os.path.join(DATA_IPFS, 'hamster_build.yaml'))  # 读取yaml文件中的测试数据
    # ids2 = ['测试{}'.format(case['case_title']) for case in cases2]
    #
    # @allure.suite('IPFS生态构建合约')
    # @allure.description("IPFS生态构建合约")
    # @pytest.mark.parametrize('case', cases2, ids=ids2)
    # def test_build(self, case):
    #     allure.dynamic.title(case['case_title'])
    #     allure.attach(body=case['url'], name='请求路径')
    #     self.driver.get(case['url'])  # 输入项目地址
    #     time.sleep(3)
    #     # 点击编译按钮
    #     self.driver.find_element(By.XPATH, case['element']['em1']).click()
    #     time.sleep(1)
    #     self.driver.refresh()  # 刷新网页
    #     time.sleep(1)
    #     # 判断代码是否检查成功
    #     tm = 0
    #     while tm < 100:
    #         time.sleep(3)
    #         tx = self.driver.find_element(By.XPATH, case['element']['em2']).text
    #         if 'Success' not in tx:
    #             time.sleep(3)
    #         else:
    #             break
    #         tm += 1
    #     time.sleep(3)
    #
    #     tx1 = self.driver.find_element(By.XPATH, case['element']['em3']).text
    #     new_url = self.driver.current_url
    #     try:
    #         assert case['text']['tx1'] in tx1
    #         assert case['new_url'] in new_url
    #         logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title']))
    #     except AssertionError as e:
    #         get_picture(self.driver, case['case_title'])  # 失败截图
    #         logger.error(
    #             "测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'], e))
    #         logger.exception(e)
    #         raise e
    #
    # cases3 = get_yaml_data(os.path.join(DATA_IPFS, 'hamster_deploy.yaml'))  # 读取yaml文件中的测试数据
    # ids3 = ['测试{}'.format(case['case_title']) for case in cases3]
    #
    # @allure.suite('IPFS生态部署合约')
    # @allure.description("IPFS生态部署合约")
    # @pytest.mark.parametrize('case', cases3, ids=ids3)
    # def test_deploy(self, case):
    #     allure.dynamic.title(case['case_title'])
    #     allure.attach(body=case['url'], name='请求路径')
    #     self.driver.get(case['url'])  # 输入项目地址
    #     time.sleep(3)
    #     #  点击deploy按钮进行部署
    #     self.driver.find_element(By.XPATH, case['element']['em1']).click()
    #
    #     # 判断合约是否部署成功
    #     tm = 0
    #     while tm < 100:
    #         time.sleep(3)
    #         tx = self.driver.find_element(By.XPATH, case['element']['em2']).text
    #         if 'Success' not in tx:
    #             time.sleep(3)
    #         else:
    #             break
    #         tm += 1
    #     time.sleep(3)
    #     # 点击部署详细页面按钮
    #     self.driver.find_element(By.XPATH, case['element']['em3']).click()
    #     time.sleep(3)
    #     # 保存ops窗口页面信息
    #     ops = self.driver.current_window_handle
    #     # 点击Visit案例查看页面文本信息
    #     self.driver.find_element(By.XPATH, case['element']['em4']).click()
    #     time.sleep(3)
    #     # 获取合约展示的HTML信息
    #     html = self.driver.page_source
    #     # 切换至ops窗口
    #     self.driver.switch_to.window(ops)
    #     time.sleep(3)
    #     # 获取ops的页面文本信息
    #     tx1 = self.driver.find_element(By.XPATH, case['element']['em5']).text
    #     time.sleep(1)
    #     tx2 = self.driver.find_element(By.XPATH, case['element']['em6']).text
    #     tx3 = self.driver.find_element(By.XPATH, case['element']['em7']).text
    #     new_url = self.driver.current_url
    #     try:
    #         assert 1 == 1
    #         assert case['text']['tx1'] in tx1
    #         assert case['text']['tx2'] in tx2
    #         assert case['text']['tx3'] in tx3
    #         assert "ERR_NAME_NOT_RESOLVED" not in html
    #         assert case['new_url'] in new_url
    #         logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title']))
    #     except AssertionError as e:
    #         get_picture(self.driver, case['case_title'])  # 失败截图
    #         logger.error("测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'], e))
    #         logger.exception(e)
    #         raise e
    #
    # cases4 = get_yaml_data(os.path.join(DATA_IPFS, 'hamster_delete.yaml'))  # 读取yaml文件中的测试数据
    # ids4 = ['测试{}'.format(case['case_title']) for case in cases4]
    #
    # @allure.suite('IPFS生态删除合约')
    # @allure.description("IPFS生态删除合约")
    # @pytest.mark.parametrize('case', cases4, ids=ids4)
    # def test_delete(self, case):
    #     allure.dynamic.title(case['case_title'])
    #     allure.attach(body=case['url'], name='请求路径')
    #     self.driver.get(case['url'])  # 输入项目地址
    #     time.sleep(3)
    #     hamster = self.driver.current_window_handle  # 保存hamster窗口的句柄
    #     # 从.ini文件中获取github的用户名和密码
    #     sth = get_ini_data('github', 'storehouse')
    #     psw = get_ini_data('github', 'passwd')
    #     # 点击github链接
    #     self.driver.find_element(By.CSS_SELECTOR,
    #                              'a[href="https://github.com/{}.git"]'.format(
    #                                  '{}/{}'.format(sth, case['case_data']))).click()
    #     #                       a[href="https://github.com/daixiang11/T_Contract_EVM_ERC4907.git"]
    #     time.sleep(3)
    #     self.driver.switch_to.window(self.driver.window_handles[-1])  # 跳转至GitHub页面
    #     # 点击setting设置
    #     self.driver.find_element(By.CSS_SELECTOR,
    #                              'a[href="/{}/settings"]'.format('{}/{}'.format(sth, case['case_data']))).click()
    #     #                                          a[href="/daixiang11/T_Contract_EVM_ERC4907/settings"]
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
    #     github = self.driver.current_window_handle  # 保存github窗口的句柄
    #     time.sleep(3)
    #     # 获取删除按钮的定位元素
    #     delete = self.driver.find_element(By.XPATH, case['element']['em1'])
    #     # 滚动页面找到最下面的删除按钮
    #     self.driver.execute_script("arguments[0].scrollIntoView();", delete)
    #     # 点击删除按钮
    #     delete.click()
    #     time.sleep(3)
    #     # 确认删除
    #     self.driver.find_element(By.XPATH, '//*[@id="repo-delete-proceed-button"]/span/span').click()
    #     time.sleep(3)
    #     # 再次确认删除
    #     self.driver.find_element(By.XPATH, '//*[@id="repo-delete-proceed-button"]/span/span').click()
    #     time.sleep(3)
    #     # 输入需要删除的库名
    #     self.driver.find_element(By.XPATH, case['element']['em2']).send_keys('{}/{}'.format(sth, case['case_data']))
    #     time.sleep(3)
    #     # 点击确认删除
    #     self.driver.find_element(By.XPATH, case['element']['em3']).click()
    #     time.sleep(3)
    #     # 判断是否需要输入github密码
    #     if idelement(self.driver, 'sudo_password'):
    #         self.driver.find_element(By.ID, 'sudo_password').send_keys(psw)
    #         self.driver.find_element(By.XPATH, case['element']['em4']).click()
    #     time.sleep(3)
    #     # 判断被删除的项目在GitHub中是否存在
    #     ast = csselement(self.driver, 'a[href="/{}"]'.format('{}/{}'.format(sth, case['case_data'])))
    #     # 切换至hamster主页面
    #     self.driver.switch_to.window(hamster)
    #     self.driver.refresh()
    #     time.sleep(3)
    #     # 点击项目名称进入项目详情
    #     self.driver.find_element(By.XPATH, case['element']['em5']).click()
    #     time.sleep(3)
    #     # 刷新页面获取元素
    #     self.driver.refresh()
    #     time.sleep(3)
    #     # 点击delete按钮
    #     self.driver.find_element(By.XPATH, case['element']['em6']).click()
    #     time.sleep(3)
    #     # 点击确认删除按钮
    #     self.driver.find_element(By.XPATH, case['element']['em7']).click()
    #     time.sleep(3)
    #     self.driver.refresh()
    #     time.sleep(3)
    #     # 判断被删除的元素在该项目中是否还存在
    #     ast1 = csselement(self.driver,
    #                       'a[href="https://github.com/{}.git"]'.format('{}/{}'.format(sth, case['case_data'])))
    #     print(ast, ast1)
    #     try:
    #         assert ast is False
    #         assert ast1 is False
    #         logger.info("测试编号:{},测试标题:{},执行成功！".format(case['case_id'], case['case_title']))
    #     except AssertionError as e:
    #         get_picture(self.driver, case['case_title'])  # 失败截图
    #         logger.error("测试编号:{},测试标题:{},执行失败!实际结果:{}".format(case['case_id'], case['case_title'], e))
    #         logger.exception(e)
    #         raise e


if __name__ == '__main__':
    pytest.main(['-vs', __file__])
