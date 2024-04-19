import os
import pytest
import allure
import selene
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    browser.config.base_url = "https://oz.by"
    browser.config.timeout = 10.0
    browser.config.driver.maximize_window()
    # browser.config.window_width = 1920
    # browser.config.window_height = 1200
    yield

