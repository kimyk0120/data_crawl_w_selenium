
from selenium import webdriver
from selenium.webdriver import ActionChains  # 액션체인 활성화
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from webdriver_manager.chrome import ChromeDriverManager


def close_webdriver(driver):
    driver.quit()
    print("prcs fin")


def clear_action(driver):
    ActionBuilder(driver).clear_actions()


def driver_init(headless=False):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_argument('--start-maximized')  # 브라우저가 최대화된 상태로 실행됩니다.
    if headless:
        options.add_argument('headless')  # 헤드리스
    driver = webdriver.Chrome(service=service, options=options)
    action = ActionChains(driver)  # 드라이버에 동작을 실행시키는 명령어를 act로 지정
    return driver, action
