import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions  # 명시적 대기
from selenium.webdriver.support.ui import WebDriverWait

from url import Url
from utils import web_driver_utils as wu
from utils.logging_utils import Logger


def enable_download_headless(browser, download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)


logging = Logger().get_logger()

# URL 설정
URL = Url().get_url()

# driver init
driver, action = wu.driver_init(headless=True)


driver.get(url=URL)
driver.implicitly_wait(10)  # 묵시적 wait


title = driver.title
logging.info("start url : " + driver.current_url)
logging.info("page title : " + title)

xpat_val = '/html/body/div/div[2]/div[2]/div/div[5]/div[2]/table/tbody/tr/td[4]/a[1]'

enable_download_headless(driver, './data')


try:
    WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, xpat_val))).click()
    time.sleep(3)
except Exception as e:
    logging.error(e)

# gotit.click()
# time.sleep(2)

print("fin")

wu.close_webdriver(driver)
