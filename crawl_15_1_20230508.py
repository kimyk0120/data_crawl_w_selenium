from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions  # 명시적 대기
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from url import Url
from utils import web_driver_utils as wu
from utils.logging_utils import Logger

logging = Logger().get_logger()

# URL 설정
URL = Url().get_url()

# driver init
driver, action = wu.driver_init(headless=False)

driver.get(url=URL)

driver.implicitly_wait(1)  # 묵시적 wait

title = driver.title
logging.info("start url : " + driver.current_url)
logging.info("page title : " + title)

# select 검색 옵션 el
select = Select(
    driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/div/form/div/div/div[1]/select[1]'))

select_options = select.options
# print(len(select_options)-1)

# select 선택
select.select_by_index(len(select_options) - 1)

# get 검색 버튼 el
search_btn = driver.find_element(by=By.XPATH,
                                 value='/html/body/div/div[2]/div[2]/div/div/button[1]')

# 검색 버튼  액션
action.click(search_btn).perform()
wu.clear_action(driver)

# 검색 결과 테이블 validate
try:
    elem_table = WebDriverWait(driver, 10).until(  # 명시적 wait
        expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/table"))
    )
except Exception as e:
    logging.error("table not loaded")
    raise e
finally:
    logging.info("table loaded")

elem_thead = elem_table.find_element(by=By.TAG_NAME, value="thead")
elem_ths = elem_thead.find_element(by=By.TAG_NAME, value="tr").find_elements(by=By.TAG_NAME, value="th")

table_head_names = []

for th in elem_ths:
    logging.info(th.text)


wu.close_webdriver(driver)
