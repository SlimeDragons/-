from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.data import Data


def login(driver):
    data = Data()
    ITEM = 'user'
    _name = data.read_option(ITEM, 'name')
    _password = data.read_option(ITEM, 'password')
    """登录页面"""
    try:
        query_element(driver, 5, (By.ID, 'details-button')).click()
        query_element(driver, 5, (By.ID, 'proceed-link')).click()
    except Exception as e:
        pass
    # 输入账号密码进行登录
    query_element(driver, 10, (By.ID, 'employess_number')).send_keys(_name)
    query_element(driver, 10, (By.ID, 'employess_password')).send_keys(_password)
    query_element(driver, 10, (By.ID, 'login_btn')).click()
    try:
        query_element(driver, 5, (By.ID, 'sureid')).click()
    except Exception as e:
        pass


def query_element(driver, time, method_value):
    """在当前页面查找元素"""
    element = WebDriverWait(driver, time).until(EC.visibility_of_element_located((method_value)))
    return element
