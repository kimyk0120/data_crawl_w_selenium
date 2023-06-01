
from selenium import webdriver
from selenium.webdriver import ActionChains  # 액션체인 활성화
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from webdriver_manager.chrome import ChromeDriverManager


def close_webdriver(driver):
    driver.quit()


def clear_action(driver):
    ActionBuilder(driver).clear_actions()


def driver_init(headless=False):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = Options()
    # options.add_argument('--start-maximized')  # 브라우저가 최대화된 상태로 실행됩니다.

    # options.add_argument('--no-sandbox')
    # options.add_argument("--disable-gpu")
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--disable-setuid-sandbox')
    # options.add_argument("--disable-extensions")
    # options.add_argument('--single-process')
    options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
    # options.add_argument("--lang=ko_KR")
    # download_path = "./data"
    # download_path = "/home/centos/NIA_legal_data_crawl/data"
    # prefs = {
    #     "download.default_directory": download_path,
    # }
    # options.add_experimental_option('prefs', prefs)
    if headless:
        options.add_argument('headless')  # 헤드리스
    driver = webdriver.Chrome(service=service, options=options)
    action = ActionChains(driver)  # 드라이버에 동작을 실행시키는 명령어를 act로 지정
    return driver, action
