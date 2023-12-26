# coding=utf-8
"""
File: test_login.py
Author: bot
Created: 2023/8/28
Description:
"""
import time

import pytest, allure
from fx_module.login.login_page import LoginPage
from config import Config

#
# @allure.epic("登录模块")
# @allure.feature("欢迎页")
# @allure.title("巡检欢迎页加载情况")
# @pytest.mark.p0
# def test_inspect_welcome_page(setup_edge_driver):
#     d = setup_edge_driver
#     p = LoginPage(d)
#     p.go_to_login_page(True)
#     assert p.inspect_welcome_page()


# @allure.epic("登录模块")
# @allure.feature("登录页")
# @allure.title("二维码扫描登录")
# @pytest.mark.p0
# def test_login_by_qr(setup_edge_driver):
#     # 此条依赖接口/v2/auth/phonelogin/code, 需后端添加白名单使得接口能返回验证码
#     d = setup_edge_driver
#     p = LoginPage(d)
#     p.go_to_login_page(True)
#     assert p.inspect_welcome_page()


@allure.epic("登录模块")
@allure.feature("登录页")
@allure.title("手机号登录")
@pytest.mark.p0
def test_login_by_phone(setup_edge_driver):
    d = setup_edge_driver
    p = LoginPage(d)
    p.go_to_login_page(True)
    p.switch_to_phone()
    p.login_by_phone(Config.ACCOUNT, "123456")
    time.sleep(1)
    assert p.login_success_check_by_url()
