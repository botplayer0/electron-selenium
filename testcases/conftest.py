# coding=utf-8
"""
File: conftest.py
Author: bot
Created: 2023/8/28
Description:
"""
import os
from datetime import datetime
import inspect

import pytest, allure
from core.init_driver import FxDriver
from pytest import TestReport
from config import Config


driver = None
run_start_at: str = ""


@pytest.fixture(scope="session")
def run_test_time():
    global run_start_at
    now = datetime.now()
    run_start_at = now.strftime("%m_%d_%H_%M_%S")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result: TestReport = outcome.get_result()
    if result.when == "call" and result.failed:
        if hasattr(driver, "get_screenshot_as_file"):
            result_path = os.path.join(Config.FAIL_IMAGE_PATH, run_start_at)
            if not os.path.exists(result_path):
                os.makedirs(result_path)
            png_path = os.path.join(result_path, f"{result.head_line}.png")
            driver.get_screenshot_as_file(png_path)
            allure.attach.file(png_path, f"错误截图: {result.head_line}")


@pytest.fixture(scope="session")
def setup_edge_driver(run_test_time):
    global driver
    driver = FxDriver.setup_edge_driver()
    yield driver
    driver.quit()


