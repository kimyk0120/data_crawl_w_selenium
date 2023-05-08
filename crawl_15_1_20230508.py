from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions  # 명시적 대기
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from url import Url
from utils import webdriver_utils as wu

URL = Url().get_url()

driver, act = wu.driver_init(headless=False)

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
wu.action_clear(driver)

# driver.implicitly_wait(5)

try:
    elem = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/table"))
    )
finally:
    print("table loaded")

wu.close_webdriver(driver)
