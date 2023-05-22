import pytest, os
from comms.constants import REPORT_JSON, REPORT_HTML, CASE_LOGIN, CASE_CONTRACT

"""
运行指定case模块和案例同时生成测试报告
1.此框架是通过pytest+seleium+allure报告来实现的UI自动化脚本，代码运行前需要配置我们所需的第三方库已经webdriver的驱动才可操作
2.由于本项目涉及到浏览器的插件操作，所以需要读取电脑的配置文件信息，比如我们可以在谷歌浏览器中的地址栏输入chrome://version来查看默认配置文件路径，
  然后将路径存放在confing.ini配置文件中
3.如果在不同的电脑端进行自动化测试，首先需要下载好插件，同时先手动登录下自己的账号，在。ini文件把配置信息更改为自己的信息
4.提示由于我们控制浏览的时候需要读取配置文件，所以代码运行前需要确保浏览器是关闭状态的，比如我运行的是Chrome浏览器，所以在运行前要关闭后台的所有Chrome
"""
# 登录模块用例：CASE_LOGIN
# evm模块测试用例：CASE_CONTRACT
# Frontend_IPFS模块测试用例：CASE_IPFS
if __name__ == '__main__':
    pytest.main(['-vs', '--alluredir', REPORT_JSON, '--clean-alluredir', CASE_LOGIN])
    os.system('allure generate %s -o %s --clean' % (REPORT_JSON, REPORT_HTML))
