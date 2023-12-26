# coding=utf-8
"""
File: init_driver.py
Author: bot
Created: 2023/8/28
Description:
"""
from utils.log import logger
import selenium.webdriver.chrome.service as service
import selenium.webdriver.edge.service as edge_service
from selenium.webdriver import ChromeOptions, EdgeOptions
from selenium import webdriver
from config import Config


class FxDriver:

    @staticmethod
    def setup_driver(app_path: str) -> webdriver.Chrome:
        logger.info(f"初始化驱动 => {app_path}")
        server = service.Service(app_path)
        opts = ChromeOptions()
        opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(service=server, options=opts)
        return driver

    @staticmethod
    def setup_edge_driver() -> webdriver.Edge:
        # logger.info(f"初始化驱动 => {app_path}")
        server = edge_service.Service(executable_path=Config.EDGE_116_PATH)
        opts = EdgeOptions()
        opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Edge(service=server, options=opts)
        return driver


if __name__ == '__main__':
    print(Config.EDGE_116_PATH)
    d = FxDriver.setup_edge_driver(Config.EDGE_116_PATH)

    d.get("https://www.baidu.com")
