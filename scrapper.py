from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import lxml

# TODO: Open dart page & Search 쌍용양회공업, 3년, 정기공시, 사업보고서
# TODO: Extract Operating income -> case1
# TODO: Extract Revenue
# TODO: Extract Net income
# TODO: Extract controlling interest

URL = "http://dart.fss.or.kr/"
PATH = "/usr/bin/chromedriver"


def get_text(name):
    driver = webdriver.Chrome(PATH)
    driver.get(URL)
    driver.find_element(By.ID, "textCrpNm").send_keys(name)
    driver.find_element_by_xpath('//a[@href="#cal8"]').click()
    driver.find_element_by_xpath('//a[@href="#divPublicType_01"]').click()
    driver.find_element(By.ID, "publicType1").click()
    driver.find_element_by_xpath('//input[@type="image"][@alt="검색"]').send_keys(Keys.ENTER)
    driver.quit()

    return

