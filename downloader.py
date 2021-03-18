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

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option("prefs", {"download.default_directory": "/mnt/f/financial_doc"})

# Search company
# Open report
# get file


def get_file(num, driver):
    driver.find_elements_by_xpath('//a[@title="사업보고서 공시뷰어 새창"]')[num].click()
    popup_window = driver.window_handles[1]
    driver.switch_to.window(popup_window)
    driver.find_element_by_xpath('//a[@href="#download"]').click()
    driver.close()
    popup_window = driver.window_handles[1]
    driver.switch_to.window(popup_window)
    driver.find_element_by_xpath("//a").click()
    driver.close()
    return


def get_files(name):
    driver = webdriver.Chrome(PATH, chrome_options=options)
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
    return

