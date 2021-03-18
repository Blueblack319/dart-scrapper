from os import path
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import lxml

URL = "http://dart.fss.or.kr/"
PATH = "/usr/bin/chromedriver"

# Search company
# Open report
# get file


def set_options():
    options = Options()
    options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": "/mnt/f/business_report",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False,
        },
    )
    # options.add_experimental_option("detach", True)
    return options


# def enable_download(driver):
#     driver.command_executor._commands["send_command"] = (
#         "POST",
#         "/session/$sessionId/chromium/send_command",
#     )
#     params = {
#         "cmd": "Page.setDownloadBehavior",
#         "params": {"behavior": "allow", "downloadPath": "/mnt/f/business_report"},
#     }
#     driver.execute("send_command", params)


def get_file(num, driver):
    driver.find_elements_by_xpath('//a[@title="사업보고서 공시뷰어 새창"]')[num].click()
    popup_window = driver.window_handles[1]
    driver.switch_to.window(popup_window)
    driver.find_element_by_xpath('//a[@href="#download"]').click()
    driver.close()
    popup_window = driver.window_handles[1]
    driver.switch_to.window(popup_window)
    driver.find_element_by_xpath("//a").click()
    time.sleep(1)
    driver.close()
    return


def get_files(name):
    options = set_options()
    driver = webdriver.Chrome(PATH, options=options)
    try:
        driver.get(URL)
        driver.find_element(By.ID, "textCrpNm").send_keys(name)
        driver.find_element_by_xpath('//a[@href="#cal8"]').click()
        driver.find_element_by_xpath('//a[@href="#divPublicType_01"]').click()
        driver.find_element(By.ID, "publicType1").click()
        driver.find_element_by_xpath('//input[@type="image"][@alt="검색"]').send_keys(Keys.ENTER)
        default_window = driver.current_window_handle
        get_file(0, driver)
        driver.switch_to.window(default_window)
        get_file(3, driver)
    finally:
        driver.quit()
    return

