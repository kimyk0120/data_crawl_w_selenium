import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from url import Url

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains  # 액션체인 활성화
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support import expected_conditions  # 명시적 대기
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

URL = Url.get_url()

service = ChromeService(executable_path=ChromeDriverManager().install())
options = Options()
options.add_argument('--start-maximized')  # 브라우저가 최대화된 상태로 실행됩니다.
# options.add_argument('headless')  # 헤드리스
driver = webdriver.Chrome(service=service, options=options)
act = ActionChains(driver)  # 드라이버에 동작을 실행시키는 명령어를 act로 지정

driver.get(url=URL)

driver.implicitly_wait(1)

title = driver.title
print("start url.py : ", driver.current_url)
print("page title : ", title)

# 검색 옵션
select = Select(
    driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/div/form/div/div/div[1]/select[1]'))

select_options = select.options
# print(len(select_options)-1)
select.select_by_index(len(select_options) - 1)


# 검색 버튼
search_btn = driver.find_element(by=By.XPATH,
                                 value='/html/body/div/div[2]/div[2]/div/div/button[1]')

# 검색 액션
act.click(search_btn).perform()
ActionBuilder(driver).clear_actions()

# driver.implicitly_wait(5)

try:
    elem = WebDriverWait(driver, 30).until(
        expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/table"))
    )
finally:
    print("table loaded")

print("prcs fin")
driver.quit()
