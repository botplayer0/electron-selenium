# coding=utf-8
"""
File: base.py
Author: bot
Created: 2023/8/28
Description:
"""
from typing import Union, List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from utils.log import logger
from config import Config
import allure


class Base:

    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME,
        'link': By.LINK_TEXT,
        'tag': By.TAG_NAME,
    }

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.WAIT = WebDriverWait(self.driver, Config.WAIT_TIME)
        self.attach = allure.attach

    def save_image(self, name: str):
        self.driver.save_screenshot(f"{Config.FAIL_IMAGE_PATH}/{name}.png")

    def find_element_by_test_id(self, locator: str) -> WebElement:
        try:
            logger.info(f"查找元素 => {locator}")
            return self.driver.find_element(By.CSS_SELECTOR, f"[data-testid='{locator}']")
        except Exception as e:
            logger.error(f"元素不存在 => {locator}")
            return False

    def find_element(self, locator: Union[str, tuple]) -> WebElement:
        try:
            if isinstance(locator, str):
                return self.find_element_by_test_id(locator)
            else:
                return self.driver.find_element(*locator)
        except Exception as e:
            logger.error(f"元素不存在 => {locator}")
            return False

    def find_element_exists(self, locator: Union[str, tuple]) -> Union[WebElement, bool]:
        try:
            if isinstance(locator, str):
                ele = self.WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"[data-testid='{locator}']")))
            else:
                ele = self.WAIT.until(EC.presence_of_element_located(*locator))
            return ele
        except Exception as e:
            logger.error(f"元素不存在 => {locator}")
            return False

    def find_elements_exists(self, locator: Union[str, tuple]) -> Union[List[WebElement], bool]:
        try:
            if isinstance(locator, str):
                ele = self.WAIT.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, f"[data-testid='{locator}']")))
            else:
                ele = self.WAIT.until(EC.presence_of_all_elements_located(*locator))
            return ele
        except Exception as e:
            logger.error(f"元素不存在 => {locator}")
            return False
