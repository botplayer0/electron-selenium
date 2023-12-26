# coding=utf-8
"""
File: login_page.py
Author: bot
Created: 2023/8/28
Description:
"""
import re
import time

import allure

from config import Config
from core.base import Base
from core.init_driver import FxDriver
from fx_module.login.consts import *
from utils.log import logger


class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_login_page(self, force: bool = False) -> bool:
        if force:
            logger.debug(f"强制跳转到登录页面")
            # 清理缓存实现强制跳转到登录页面
            self.driver.execute_script("window.localStorage.removeItem('auth');")
            self.driver.get(Config.BASE_URL + Config.LOGIN_URL)
        else:
            self.driver.get(Config.BASE_URL + Config.LOGIN_URL)
        if force:
            if "/login" not in self.driver.current_url:
                logger.error(f"跳转到登录页面失败")
                return False
        return True

    def is_qr_code_page(self):
        logger.debug("判断是否为二维码登录页面")
        return self.find_element_exists(QR_CODE_PAGE)

    def is_phone_page(self):
        logger.debug("判断是否为手机登录页面")
        return self.find_element_exists(PHONE_PAGE)

    def switch_to_phone(self):
        logger.debug("切换到手机登录页面")
        self.find_element(SWITCH_TO_PHONE).click()

    def switch_to_qr_code(self):
        logger.debug("切换到二维码登录页面")
        self.find_element(SWITCH_TO_QR).click()

    def login_by_phone(self, phone, code):
        logger.debug("使用手机号登录")
        self.find_element(PHONE_INPUT).send_keys(phone)
        self.find_element(PHONE_CODE).send_keys(code)
        self.find_element(LOGIN_BTN).click()

    def inspect_welcome_page(self):
        logger.debug("巡检欢迎页")
        img_list = self.find_elements_exists(WELCOME_PAGE)
        img_loaded_result = True
        for img in img_list:
            if img.get_attribute("naturalWidth") == "0":
                logger.error(f"巡检欢迎页-图片加载失败: {img.get_attribute('src')}")
                img_loaded_result = False
        if img_loaded_result:
            # self.attach.file("欢迎页图片加载失败", self.driver.get_screenshot_as_png(), allure.attachment_type)
            pass
        return img_loaded_result

    def login_success_check_by_url(self):
        logger.debug("通过URL检查是否登录成功")
        c_url = self.driver.current_url
        pattern = re.compile(".*board.*")
        if pattern.match(c_url):
            logger.debug("登录成功")
            return True
        return False



if __name__ == '__main__':
    d = FxDriver.setup_edge_driver()
    p = LoginPage(d)
    p.inspect_welcome_page()
    # print(p.go_to_login_page(force=True))
    # if p.is_qr_code_page():
    #     p.switch_to_phone()
    #     p.login_by_phone(Config.ACCOUNT, "")
    #

    # if p.is_phone_page():
    #     p.switch_to_qr_code()