import os

"""
使用常量对路径进行管理
好处: 代码使用非绝对路径,可移植性高
"""

# 获取项目路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 测试用例执行文件所在路径
CASE_DIR = os.path.join(BASE_DIR, r'test_cases')
CASE_LOGIN = os.path.join(CASE_DIR, r'test_login\test_login.py')
CASE_CONTRACT = os.path.join(CASE_DIR, r'test_contract\test_contract_evm.py')
CASE_IPFS = os.path.join(CASE_DIR, r'test_frontend\test_frontend_ipfs.py')
# 测试数据所在路径
DATA_DIR = os.path.join(BASE_DIR, 'datas')
DATA_YAML = os.path.join(DATA_DIR, 'hamster_login.yaml')
CONTRACT = os.path.join(DATA_DIR, 'contract_evm')
DATA_CONTRACT_EVM_CREATE = os.path.join(CONTRACT, 'hamster_create_evm.yaml')
DATA_CONTRACT_EVM_CHECK = os.path.join(CONTRACT, 'hamster_check_evm.yaml')
DATA_CONTRACT_EVM_BUILD = os.path.join(CONTRACT, 'hamster_build_evm.yaml')
DATA_CONTRACT_EVM_DEPLOY = os.path.join(CONTRACT, 'hamster_deploy_evm.yaml')
DATA_CONTRACT_EVM_DELETE = os.path.join(CONTRACT, 'hamster_delete_evm.yaml')
DATA_IPFS = os.path.join(DATA_DIR, 'frontend_ipfs')
DATA_CONTAINER = os.path.join(DATA_DIR, 'frontend_container')

# log所在路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')
INFO_FILE = os.path.join(LOG_DIR, 'info.log')
ERROR_FILE = os.path.join(LOG_DIR, 'error.log')

# 测试报告所在路径
REPORT_DIR = os.path.join(BASE_DIR, 'reports')
REPORT_JSON = os.path.join(REPORT_DIR, 'allure_json')
REPORT_HTML = os.path.join(REPORT_DIR, 'allure_html')

# 测试截图所在路径
PICTURE_DIR = os.path.join(BASE_DIR, 'picture')

# 获取config.ini目录
CFI = os.path.join(BASE_DIR, 'confs/confing.ini')

if __name__ == '__main__':
    print(BASE_DIR)
    print(CASE_DIR)
    print(DATA_YAML)
    print(REPORT_DIR)
    print(ERROR_FILE)
