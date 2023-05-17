import time
from hamster_test.comms.yaml_utils import get_picture
from hamster_test.comms.hamster.opject import Hamster
from selenium.webdriver.common.by import By
from selenium import webdriver
from hamster_test.comms.log_utils import get_logger
from hamster_test.comms.yaml_utils import get_ini_data
from hamster_test.comms.hamster.elenium import elenium as em


class CreateProject(Hamster):
    # git登录页面的操作
    def longin(self, value1, value2):
        """

        :param value1: 输入用户名或者邮箱账户
        :param value2: 输入密码
        :return:
        """
        if self.iselement(5, *em.login_github):
            self.click(10, *em.login_github)
            self.window(-1)
            if self.iselement(10, *em.sed_login):
                self.send_keys(10, *em.sed_login, value1)
                self.send_keys(10, *em.sed_password, value2)
                self.click(10, *em.click_commit)
            if self.iselement(5, *em.github_empower):
                self.clicks(10, *em.github_empower)
        self.window(0)
        # if self.iselement(10, *em.create_project):
        #     self.click(5, *em.create_project)

    # 打开evm合约的项目展示
    def open_evm(self):
        self.target(10, *em.create_next)

    # 打开aptos合约的项目展示
    def open_aptos(self):
        time.sleep(3)
        self.driver.find_element(*em.create_aptos).click()
        time.sleep(3)
        self.target(10, By.XPATH, *em.create_next)

    # 打开starkware合约的项目展示
    def open_starkware(self):
        time.sleep(3)
        self.driver.find_element(*em.create_starkware).click()
        time.sleep(3)
        self.target(10, *em.create_next)

    # 打开sui合约的项目展示
    def open_sui(self):
        time.sleep(3)
        self.driver.find_element(*em.create_sui).click()
        time.sleep(3)
        self.target(10, *em.create_next)

    # 打开前端Ipfs合约的项目展示
    def open_frontend_ipfs(self):
        time.sleep(3)
        self.driver.find_element(*em.create_frontend).click()
        time.sleep(3)
        self.target(10, *em.create_next)

    # 打开前端container合约的项目展示
    def open_frontend_container(self):
        time.sleep(3)
        self.driver.find_element(*em.create_frontend).click()
        time.sleep(3)
        self.driver.find_element(*em.create_container).click()
        time.sleep(3)
        self.target(10, *em.create_next)

    # 创建项目合约的操作页面
    def create_by_template(self, value):
        """

        :param value:创建项目的名称
        :return:
        """
        self.click(10, *em.create_by_template)
        self.send_keys(10, *em.send_project_name, value)
        self.click(10, *em.click_create)

    # 点击所选项目的详情页面
    def contract_projects(self, name, len):
        """

        :param name: 项目名称
        :param len: 创建项目的数量
        :return:
        """
        for i in range(len):
            tx = self.text(10, *em.project_contract_names[i])
            if name in tx:
                self.click(5, *em.project_contract_names[i])
                break

    # 点击项目检查的check按钮
    def contract_check(self, name, len):
        """

        :param name:项目名称
        :param len: 创建项目的数量
        :return:
        """
        for i in range(len):
            tx = self.text(10, *em.project_contract_names[i])
            if name in tx:
                self.click(5, *em.project_contract_checks[i])
                break

    # 点击项目构建按钮
    def contract_build(self, name, len):
        """

          :param name:项目名称
          :param len: 创建项目的数量
          :return:
          """
        for i in range(len):
            tx = self.text(5, *em.project_contract_names[i])
            if name in tx:
                self.click(5, *em.project_contract_builds[i])
                time.sleep(3)
                break

    # 点击项目合约部署deploy按钮
    def contract_deploy(self, name, len):
        """

          :param name:项目名称
          :param len: 创建项目的数量
          :return:
        """
        for i in range(len):
            tx = self.text(5, *em.project_contract_names[i])
            if name in tx:
                self.click(5, *em.project_contract_deploys[i])
                break

    # 点击项目的合约调用ops按钮
    def contract_ops(self, name, len):
        """

          :param name:项目名称
          :param len: 创建项目的数量
          :return:
        """
        for i in range(len):
            tx = self.text(5, *em.project_contract_names[i])
            if name in tx:
                self.click(5, *em.project_contract_ops[i])
                break

    # 等待加载的状态是否成功
    def wait_recent(self, times, path, element):
        try:
            tm = 0
            while tm < times:
                time.sleep(3)
                tx = self.text(10, path, element)
                if 'Success' in tx:
                    break
                tm += 1
        except Exception as e:
            print('运行时间过长')
            get_picture(self.driver, '检查或编译过长')  # 失败截图
            get_logger().error("检查或编译过长")
            raise e

    # 链接小狐狸钱包的登录操作
    def metamask_login(self, value):
        self.driver.implicitly_wait(15)
        windows = self.driver.window_handles
        # 判断钱包是否自动弹出
        if len(windows) >= 2:
            self.window(1)
            self.send_keys(10, *em.metamask_passwd, value)
            self.click(10, *em.metamask_login)
            self.window(0)
        # 判断钱包是否已经链接
        if self.iselement(1, *em.connect_wallet):
            self.click(5, *em.connect_wallet)
            time.sleep(1)
            shadow = self.driver.execute_script(em.js)
            time.sleep(3)
            windows = self.driver.window_handles
            # 判断钱包是否需要输入密码
            if len(windows) > 1:
                self.window(1)
                self.send_keys(10, *em.metamask_passwd, value)
                self.click(10, *em.metamask_login)
                self.window(0)

    # 部署evm的页面操作
    def deploy_evm(self, int1, int2):
        self.click(10, *em.deploy_evm_name)
        self.click(10, *em.deploy_evm_chain)
        self.click(10, *em.deploy_evm_chains[int1 - 1])
        self.click(10, *em.deploy_evm_network)
        self.click(10, *em.deploy_evm_networks[int2 - 1])
        self.click(10, *em.deploy_evm_click)

    # 部署evm的nft合约操作页面
    def deploy_evm_nft(self, value1, value2, value3, int1, int2):
        self.click(10, *em.deploy_evm_name_nft)
        self.send_keys(10, *em.deploy_evm_name_nfts[0], value1)
        self.send_keys(10, *em.deploy_evm_name_nfts[1], value2)
        self.send_keys(10, *em.deploy_evm_name_nfts[2], value3)
        self.click(10, *em.deploy_evm_name_nfts[3])
        self.click(10, *em.deploy_evm_chain)
        self.click(10, *em.deploy_evm_chains_nft[int1 - 1])
        self.click(10, *em.deploy_evm_network)
        self.click(10, *em.deploy_evm_networks_nft[int2 - 1])
        self.click(10, *em.deploy_evm_click)

    # 确认部署页面操作
    def deploy_evm_confirm(self, value):
        time.sleep(3)
        self.window(-1)
        if self.iselement(10, *em.metamask_passwd):
            self.send_keys(10, *em.metamask_passwd, value)
            self.click(10, *em.metamask_login)
            time.sleep(3)
            a = self.driver.window_handles
            if len(a) >= 2:
                self.window(-1)
                self.clicks(10, *em.metamask_confirm)
        if self.iselement(5, *em.metamask_know):
            self.clicks(10, *em.metamask_know)
        if self.iselement(5, *em.metamask_handoff):
            self.clicks(10, *em.metamask_handoff)
        time.sleep(3)
        self.window(0)
        if self.iselement(10, *em.deploy_evm_click):
            self.clicks(10, *em.deploy_evm_click)
            time.sleep(3)
            self.window(1)
            self.clicks(10, *em.metamask_confirm)

    # 删除github中的项目的页面操作
    def delete_project_github(self, sth, case, value):
        """

        :param sth: github的仓库名称
        :param case: 仓库中需要删除的项目名称
        :param value: 需要输入的仓库与项目名
        :return:
        """
        # 点击setting设置
        self.click(10, By.CSS_SELECTOR, 'a[href="/{}/settings"]'.format('{}/{}'.format(sth, case)))
        # 点击删除按钮
        self.target(10, *em.delete_this_repository)
        # 确认删除
        self.click(10, *em.delete_want)
        # 再次确认删除
        self.clicks(10, *em.delete_want)
        # 输入需要删除的库名
        self.send_keys(10, *em.delete_box, value)
        # 点击确认删除
        self.clicks(10, *em.delete_this_repository_to)

    # 判断删除github项目是否需要输入密码
    def delete_project_passwd(self, passwd):
        """

        :param passwd:所属github的密码
        :return:
        """
        if self.iselement(10, *em.delete_sudo_password):
            self.send_keys(10, *em.delete_sudo_password, passwd)
            self.click(10, *em.delete_password_submit)

    # 操作删除hamster的project项目
    def delete_project_hamster(self):
        self.click(10, *em.projects_hamster_delete)
        self.clicks(10, *em.projects_hamster_delete_yes)

    # 打开前端项目的展示模板并且返回对应的网页信息
    def get_frontend_view(self, path, element, num):
        """
        点击view获取view视图中的文本信息
        :param path: view按钮的元素属性
        :param element: view按钮的元素
        :num:获取视图的的标号
        :return: view打开的页面的值
        """
        self.click(10, path, element)
        self.driver.implicitly_wait(15)
        self.window(1)
        tx = self.text(10, *em.frontend_view[num - 1])
        self.window(0)
        return tx

    # metatrust检查弹窗页面
    def run_metatrust_evm(self, sa1=None, sa2=None, sa3=None, osa1=None, cqa1=None, cqa2=None, gua1=None, ai=None):
        """
        metatrust 检查工具的选择
        :param sa1: Mythril
        :param sa2: MetaTrust Security Analyzer
        :param sa3: MetaTrust Security Prover
        :param osa1: MetaTrust Open Source Analyzer
        :param cqa1: Solhint
        :param cqa2: MetaTrust Code Quality
        :param gua1: eth-gas-reporter
        :param ai: AI
        :return:
        """
        if self.iselement(10, *em.project_check_metatrust_done):
            if sa1 == "sa1":
                self.click(10, *em.project_check_metatrust[0])
            if sa2 == "sa2":
                self.click(10, *em.project_check_metatrust[1])
            if sa3 == "sa3":
                self.click(10, *em.project_check_metatrust[2])
            if osa1 == "osa1":
                self.click(10, *em.project_check_metatrust[3])
            if cqa1 == "cqa1":
                self.click(10, *em.project_check_metatrust[4])
            if cqa2 == "cqa2":
                self.click(10, *em.project_check_metatrust[5])
            if gua1 == "gua1":
                self.click(10, *em.project_check_metatrust[6])
            if ai == "ai":
                self.click(10, *em.project_check_metatrust[7])
            if sa1 != "sa1" and sa2 != "sa2" and sa3 != "sa3" and osa1 != "osa1" and cqa1 != "cqa1" and cqa2 != "cqa2" and gua1 != "gua1" and ai != "ai":
                print('metatrust 的检查工具需要选择对应的工具才能运行')
                raise AssertionError
            self.click(10, *em.project_check_metatrust_done)


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_argument(
        "--user-data-dir=" + get_ini_data('version', 'chrome_Default'))  # 添加获取到的配置文件路径
    option.add_experimental_option('detach', True)  # 浏览器不会自动关闭
    driver = webdriver.Chrome(chrome_options=option, options=option)  # 打开配置插件的chrome浏览器
    driver.maximize_window()  # 浏览器窗口最大化
    cp = CreateProject(driver)
    cp.geturl('https://develop.hamster.newtouch.com/projects')
    #
    cp.longin('983643937@qq.com', 'Dx3826729')
    print('remote_url:', driver.caps['goog:chromeOptions']['debuggerAddress'])
    # cp.open_evm()
    # cp.click(10, *em.evm_nfts2)
    # cp.create_by_template('test0003')
    # cp.click(30, By.XPATH, '//*[@id="layout-default"]/section/main/div[2]/button/span')
    cp.contract_check('test0002', 5)
    cp.contract_build('test0002', 1)
    cp.contract_deploy('test0002', 1)
    time.sleep(3000)
