from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import lxml


# Open dart page & Search 쌍용양회공업, 3년, 정기공시, 사업보고서
# TODO: Extract Operating income -> case1
# TODO: Extract Revenue
# TODO: Extract Net income
# TODO: Extract controlling interest

URL = "http://dart.fss.or.kr/"
PATH = "/usr/bin/chromedriver"

options = Options()
options.add_experimental_option("detach", True)


def get_text(name):
    driver = webdriver.Chrome(PATH, chrome_options=options)
    driver.get(URL)
    driver.find_element(By.ID, "textCrpNm").send_keys(name)
    driver.find_element_by_xpath('//a[@href="#cal8"]').click()
    driver.find_element_by_xpath('//a[@href="#divPublicType_01"]').click()
    driver.find_element(By.ID, "publicType1").click()
    driver.find_element_by_xpath('//input[@type="image"][@alt="검색"]').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//a[@title="사업보고서 공시뷰어 새창"]').click()
    report_window = driver.window_handles[1]
    driver.switch_to.window(report_window)
    driver.find_element_by_xpath(
        '//div[@class="x-tree-root-node"]/li[5]//li[2]//a[@class="x-tree-node-anchor"]'
    ).click()
    consolidated_financial_statements = driver.page_source
    soup = BeautifulSoup(consolidated_financial_statements, "lxml")

    return

