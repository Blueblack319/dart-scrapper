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
# TODO: Open report
# TODO: get file

def open_report(name):

def get_file():


def get_files(name):
    driver = webdriver.Chrome(PATH, chrome_options=options)
    driver.get(URL)
    driver.find_element(By.ID, "textCrpNm").send_keys(name)
    driver.find_element_by_xpath('//a[@href="#cal8"]').click()
    driver.find_element_by_xpath('//a[@href="#divPublicType_01"]').click()
    driver.find_element(By.ID, "publicType1").click()
    driver.find_element_by_xpath('//input[@type="image"][@alt="검색"]').send_keys(Keys.ENTER)

    driver.find_elements_by_xpath('//a[@title="사업보고서 공시뷰어 새창"]')[3].click()
    f_report_window = driver.window_handles[1]
    driver.switch_to.window(f_report_window)
    driver.find_element_by_xpath('//a[@href="#download"]').click()
    f_download_window = driver.window_handles[2]
    driver.switch_to.window(f_download_window)
    driver.find_element_by_xpath("//a").click()

    return

