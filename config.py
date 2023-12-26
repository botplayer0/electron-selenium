# coding=utf-8
"""
File: config.py
Author: bot
Created: 2023/8/28
Description:
"""

import os


ROOT = os.path.dirname(__file__)


class BaseConfig:

    DRIVER_PATH: str = os.path.join(ROOT, "driver_file")
    EDGE_116_PATH: str = os.path.join(DRIVER_PATH, "edge_116", "msedgedriver")

    # Allure配置
    FAIL_IMAGE_PATH: str = os.path.join(ROOT, "result")

    # selenium 等待
    WAIT_TIME: int = 5

    # 飞项配置
    ACCOUNT: str = "18318911515"
    BASE_URL: str = "http://localhost:4200"
    LOGIN_URL: str = "/login"


Config = BaseConfig()

if __name__ == '__main__':
    print(ROOT)