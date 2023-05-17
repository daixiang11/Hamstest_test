from selenium.webdriver.common.by import By

"""
Hamster主控制栏元素
"""
# HAMSTER图标
hamster = (By.XPATH, '//*[@id="layout-default"]/div/div[1]/div[1]/img[1]')
# projects按钮
projects = (By.ID, 'pro')
# Middleware按钮
middleware = (By.ID, 'middle')
# Dashboard按钮
dashboard = (By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div/div/ul/li[1]/span')
# Miwaspace按钮
miwaspace = (By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div/div/ul/li[2]/span')
# Ethereum Mainnet按钮
ethereum_mainnet = (By.XPATH, '//*[@id="layout-default"]/div/div[2]/div[2]/div/div/span[2]')
# Connect Wallet 链接钱包按钮
connect_wallet = (By.XPATH, '//*[@id="layout-default"]/div/div[2]/div[3]/button')
# 登录小狐狸钱包的页面元素
js = """document.querySelector("body > onboard-v2").shadowRoot.querySelector("div[class='wallet-button-container-inner svelte-1vlog3j']").click()"""
# 小狐狸钱包输入密码
metamask_passwd = (By.ID, 'password')
# 小狐狸钱包点击登录按钮
metamask_login = (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/button')
# 小狐狸钱包点击切换按钮
metamask_handoff = (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div/button[2]')
# 小狐狸钱包点击确认交易按钮
metamask_confirm = (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/div[3]/footer/button[2]')
# 小狐狸钱包点击已经知晓按钮
metamask_know = (By.XPATH, '//*[@id="popover-content"]/div/div/section/div[3]')
"""
github登录页面的元素
"""
# 点击github登录按钮
login_github = (By.XPATH, "//*[@id='app']/div/div[2]/div[2]/span")
# 输入邮箱账号
sed_login = (By.NAME, 'login')
# 输入密码
sed_password = (By.NAME, 'password')
# 点击提交按钮
click_commit = (By.NAME, 'commit')
# github授权按钮
github_empower = (By.XPATH, '//*[@id="js-oauth-authorize-btn"]')
"""
github操作页面元素
"""
# 设置里面的delete this repository按钮
delete_this_repository = (By.XPATH, '//*[@id="dialog-show-repo-delete-menu-dialog"]/span/span')
# 点击确认删除项目仓库的按钮
delete_want = (By.XPATH, '//*[@id="repo-delete-proceed-button"]/span/span')
# 输入需要删除的项目名称的输入框
delete_box = (By.XPATH, '//*[@id="verification_field"]')
# 确认删除按钮
delete_this_repository_to = (By.XPATH, '//*[@id="repo-delete-proceed-button"]/span/span')
# 删除项目时输入密码输入框
delete_sudo_password = (By.ID, 'sudo_password')
# 删除项目时确认提交密码按钮
delete_password_submit = (By.XPATH, '//*[@id="sudo"]/sudo-credential-options/div[2]/form/div/div/button')

"""
createprojects创建项目首页的页面
"""
# 项目首页的cerateproject按钮
create_project = (By.XPATH, '//*[@id="layout-default"]/section/main/div[1]/div[1]/button')
# 创建项目首页的Next按钮
create_next = (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div[2]/button')
# 创建项目首页的aptos点击框
create_aptos = (By.XPATH, '//*[@id="form_item_frameType"]/label[2]/span[1]/input')
# 创建项目首页的starkware点击框
create_starkware = (By.XPATH, '//*[@id="form_item_frameType"]/label[4]/span[1]/input')
# 创建项目首页的sui点击框
create_sui = (By.XPATH, '//*[@id="form_item_frameType"]/label[5]/span[1]/input')
# 创建前端项目首页的frontend点击框
create_frontend = (By.XPATH, '//*[@id="form_item_type"]/label[2]/span[1]/input')
# 创建前端项目首页的container点击框
create_container = (By.XPATH,
                    '//*[@id="layout-default"]/section/main/div/div[2]/div[1]/form/div[4]/div[2]/div/div/div/label['
                    '2]/span[1]/input')
"""
EVM创建EVM项目的页面元素
"""
# 创建evm合约中的项目元素
evm_nfts = [
    (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div[1]/div[1]/div[3]/div[1]'),
    (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div/div[1]/div[3]/div[2]'),
    (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div/div[1]/div[3]/div[3]'),
    (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div/div[1]/div[3]/div[4]'),
    (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div[1]/div[4]/div[3]/div')]
# 创建chainlink合约项目的元素
evm_chainlink = (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div[1]/div[5]/div[3]/div')
"""
创建前端项目的页面元素
"""
# 前端ipfs的项目创建展示页面的元素
frontend_ipfs = [(By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div/div/div[3]/div[1]'),
                 (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div/div/div[3]/div[2]')]

"""
创建项目弹窗页面的元素
"""
# 创建项目的按钮
create_by_template = (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[1]/div[2]/button[3]')
# 下载合约的按钮
download = (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[1]/div[2]/button[2]')
# 创建项目中的弹窗元素
send_project_name = (By.CLASS_NAME, 'ant-input')
click_create = (By.ID, 'create-project-btn')
# 返回项目的页面按钮
back_to_project = (By.XPATH, '//*[@id="layout-default"]/section/main/div[2]/button/span')

"""
项目管理页面的元素
"""
# 项目管理页面的名称元素
project_contract_names = [(By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[1]/div/div[1]/div[1]/div/div[1]'),
                          (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[2]/div/div[1]/div[1]/div/div[1]'),
                          (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[3]/div/div[1]/div[1]/div/div[1]'),
                          (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[4]/div/div[1]/div[1]/div/div[1]'),
                          (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[5]/div/div[1]/div[1]/div/div[1]')]
project_contract_name1 = (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[1]/div/div[1]/div[1]/div/div[1]')
# 显示项目检查运行状态的按钮
project_contract_recent_check = [
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/div'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[4]/div/div/div[2]/div/div[2]/div[2]/div'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[5]/div/div/div[2]/div/div[2]/div[2]/div')]

# 项目检查的view按钮展示检查页面的详情
project_contract_view_check = [(By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[1]/div/div/div[2]/div/div[2]/div[3]'),
                               (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[2]/div/div/div[2]/div/div[2]/div[3]'),
                               (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[3]/div/div/div[2]/div/div[2]/div[3]'),
                               (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[4]/div/div/div[2]/div/div[2]/div[3]'),
                               (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[5]/div/div/div[2]/div/div[2]/div[3]')]
# 项目管理页面的check按钮
project_contract_checks = [
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[1]/div/div/div[1]/div[2]/div/label[1]/label[3]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[2]/div/div/div[1]/div[2]/div/label[1]/label[3]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[3]/div/div/div[1]/div[2]/div/label[1]/label[3]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[4]/div/div/div[1]/div[2]/div/label[1]/label[3]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[5]/div/div/div[1]/div[2]/div/label[1]/label[3]')]
# check详情展示页面元素
check_result = (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div/div[2]/div/div[2]/div')
# 项目管理页面的build按钮
project_contract_builds = [
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[1]/div/div/div[1]/div[2]/div/label[2]/label[4]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[2]/div/div/div[1]/div[2]/div/label[2]/label[4]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[3]/div/div/div[1]/div[2]/div/label[2]/label[4]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[4]/div/div/div[1]/div[2]/div/label[2]/label[4]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[5]/div/div/div[1]/div[2]/div/label[2]/label[4]'), ]
# 显示项目build运行状态的按钮
project_contract_recent_build = [
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[1]/div/div/div[2]/div/div[3]/div[2]/div'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[3]/div/div/div[2]/div/div[3]/div[2]/div'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[4]/div/div/div[2]/div/div[3]/div[2]/div'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[5]/div/div/div[2]/div/div[3]/div[2]/div'), ]
# 显示build详情页面的按钮
project_contract_view_build = [
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[1]/div/div/div[2]/div/div[3]/div[3]/div/div'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[2]/div/div/div[2]/div/div[3]/div[3]/div/div'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[3]/div/div/div[2]/div/div[3]/div[3]/div/div'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[4]/div/div/div[2]/div/div[3]/div[3]/div/div'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[5]/div/div/div[2]/div/div[3]/div[3]/div/div')]
# build详情页面的文本元素
build_result = (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div/div[2]/div/div[2]')
"""
build详情页面的元素
"""
# build详情页面里面的deploy按钮
build_deploy = (By.XPATH,
                '//*[@id="layout-default"]/section/main/div/div[4]/div/div[2]/div['
                '2]/div/div/div/div/div/table/tbody/tr/td[5]/label[1]')

# build详情页面里面的more按钮
build_more = (By.XPATH,
              '//*[@id="layout-default"]/section/main/div/div[4]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td['
              '5]/label[2]')
# build详情页面里面的more按钮中的more——api按钮
build_more_abi = (By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div/div/div[2]/div')
# 项目管理页面的deploy按钮的元素
project_contract_deploys = [
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[1]/div/div/div[1]/div[2]/div/label[3]/label[4]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[2]/div/div/div[1]/div[2]/div/label[3]/label[4]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[3]/div/div/div[1]/div[2]/div/label[3]/label[4]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[4]/div/div/div[1]/div[2]/div/label[3]/label[4]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[5]/div/div/div[1]/div[2]/div/label[3]/label[4]')]
# 项目管理页面的ops按钮的元素
project_contract_ops = [
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[1]/div/div/div[1]/div[2]/div/label[4]/label[4]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[2]/div/div/div[1]/div[2]/div/label[4]/label[4]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[3]/div/div/div[1]/div[2]/div/label[4]/label[4]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[4]/div/div/div[1]/div[2]/div/label[4]/label[4]'),
    (By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[5]/div/div/div[1]/div[2]/div/label[4]/label[4]')]
# deploy详情页面中的name选择框
deploy_evm_name = (By.XPATH, '//*[@id="basic_nameData"]/div/label/span[1]')
# evm——nft合约的deploy详情页面中的name选择框
deploy_evm_name_nft = (By.XPATH, '//*[@id="basic_nameData"]/div/img')
# evm-nft合约的deploy详情页面中的name选择框中的下拉展开元素
deploy_evm_name_nfts = [(By.XPATH, '//*[@id="userForm_name"]'),
                        (By.XPATH, '//*[@id="userForm_symbol"]'),
                        (By.XPATH, '//*[@id="userForm_version"]'),
                        (By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button')]
# deploy详情页面中的chain选择框
deploy_evm_chain = (By.XPATH, '//*[@id="layout-default"]/section/main/div[2]/div[1]/form/div[5]/div/div/div/div[2]')
# evm-nft合约的deploy详情页面中的chain选择框中的下拉元素
deploy_evm_chains_nft = [(By.XPATH, '//*[@id="htmlRoot"]/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[1]/div'),
                         (By.XPATH, '//*[@id="htmlRoot"]/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[2]/div'),
                         (By.XPATH, '//*[@id="htmlRoot"]/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[3]/div')]
# deploy详情页面中的chain选择框中的下拉元素
deploy_evm_chains = [(By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div'),
                     (By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div'),
                     (By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[3]/div')]
# deploy详情页面中的network选择框
deploy_evm_network = (
    By.XPATH, '//*[@id="layout-default"]/section/main/div[2]/div[1]/form/div[6]/div/div/div/div[2]/div')
# deploy详情页面中的network选择框的下拉元素
deploy_evm_networks = [(By.XPATH, '//*[@id="htmlRoot"]/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[1]/div'),
                       (By.XPATH, '//*[@id="htmlRoot"]/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[2]/div'),
                       (By.XPATH, '//*[@id="htmlRoot"]/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[3]/div'),
                       (By.XPATH, '//*[@id="htmlRoot"]/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[4]/div')]
# evm-nft合约的deploy详情页面中的network选择框的下拉元素
deploy_evm_networks_nft = [(By.XPATH, '//*[@id="htmlRoot"]/body/div[4]/div/div/div/div[2]/div[1]/div/div/div[1]/div'),
                           (By.XPATH, '//*[@id="htmlRoot"]/body/div[4]/div/div/div/div[2]/div[1]/div/div/div[2]/div'),
                           (By.XPATH, '//*[@id="htmlRoot"]/body/div[4]/div/div/div/div[2]/div[1]/div/div/div[3]/div'),
                           (By.XPATH, '//*[@id="htmlRoot"]/body/div[4]/div/div/div/div[2]/div[1]/div/div/div[4]/div'), ]
# deploy详情页面中的点击提交按钮
deploy_evm_click = (By.XPATH, '//*[@id="layout-default"]/section/main/div[2]/div[2]/button')
"""
项目详情页面元素
"""
# check按钮
projects_check = (
    By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div/div/div[1]/div[2]/div/label[1]/label[3]')
# check后的状态展示
projects_recent_check = (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div/div/div[2]/div/div[2]/div[2]')
# 查看check详情按钮
projects_view_check = (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div/div/div[2]/div/div[2]/div[3]')
# build按钮
projects_build = (
    By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div/div/div[1]/div[2]/div/label[2]/label[4]')
# build后的状态展示
projects_recent_build = (
    By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div')
# 查看build的详情按钮
projects_view_build = (
    By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div/div/div[2]/div/div[3]/div[3]/div/div')
# 删除项目的delete按钮
projects_hamster_delete = (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[1]/div[2]/button[1]')
# 删除项目中的确认按钮
projects_hamster_delete_yes = (By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div[2]/div/div[2]/div/div[3]/button[2]')

"""
ops页面元素
"""
# ops整个页面的元素
ops_projects = (By.ID, 'layout-default')

"""
前端项目展示页面的元素
"""
# 创建前端项目时的展示view按钮
create_frontend_view = (By.XPATH, '//*[@id="layout-default"]/section/main/div/div[2]/div[1]/div/button')
#  前端项目展示模板页面的整个元素
frontend_view = [(By.XPATH, '//*[@id="app"]'), (By.XPATH, '//*[@id="root"]/div')]

"""
前端创建项目后的展示页面元素
"""
# 前端项目管理页面的项目名称元素
project_frontend_names = [(By.XPATH, '//*[@id="rc-tabs-0-panel-2"]/div/div[1]/div/div/div[1]/div[1]/div[1]'),
                          (By.XPATH, '//*[@id="rc-tabs-0-panel-2"]/div/div[1]/div/div/div[1]/div[1]/div[2]'),
                          (By.XPATH, '//*[@id="rc-tabs-0-panel-2"]/div/div[1]/div/div/div[1]/div[1]/div[3]'),
                          (By.XPATH, '//*[@id="rc-tabs-0-panel-2"]/div/div[1]/div/div/div[1]/div[1]/div[4]')]

"""
evm的matetrust检查的弹窗页面
"""
project_check_metatrust = [(By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div[1]/p'),
                           (By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div[2]/p'),
                           (By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div[3]/p'),
                           (By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div[2]/div/div[2]/div/div/div[4]/div/p'),
                           (By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div[2]/div/div[2]/div/div/div[5]/div[1]/p'),
                           (By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div[2]/div/div[2]/div/div/div[5]/div[2]/p'),
                           (By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div[2]/div/div[2]/div/div/div[6]/div/p'),
                           (By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div[2]/div/div[2]/div/div/div[7]/div/p')]
project_check_metatrust_done = (By.XPATH, '//*[@id="htmlRoot"]/body/div[2]/div/div[2]/div/div[2]/div/div/button')
