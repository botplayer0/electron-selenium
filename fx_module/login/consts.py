# coding=utf-8
"""
File: consts.py
Author: bot
Created: 2023/8/28
Description:
"""
from selenium.webdriver.common.by import By

# 页面
QR_CODE_PAGE = "login-qrcode-page"
PHONE_PAGE = "login-phone-page"

# 登录切换按钮, 仅测试环境存在
SWITCH_TO_PHONE = "switch-to-phone"
SWITCH_TO_QR = "switch-to-qrcode"

# 手机登录输入框以及确认登录按钮
PHONE_INPUT = (By.ID, "login_phoneNum")
PHONE_CODE = (By.ID, "login_code")
LOGIN_BTN = "login-button"

# 二维码登录按钮
RE_SCAN_BTN = "re-scan-qr-code-btn"

# 欢迎页
WELCOME_PAGE = "advertisement-img"
