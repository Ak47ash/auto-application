from contextlib import contextmanager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from undetected_chromedriver import Chrome, ChromeOptions


@contextmanager
def initialize_webdriver(headless=True):
    driver = None
    try:
        options = ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-notifications")
        options.add_argument("--start-fullscreen")
        if headless:
            options.add_argument("--headless")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option("useAutomationExtension", False)
        # capabilities = {
        #     "goog:loggingPrefs": {"performance": "ALL"}
        # }
        # options.add_experimental_option('w3c', False)
        # options.add_experimental_option('perfLoggingPrefs', capabilities)

        driver = Chrome(options=options)

        yield driver
    finally:
        if driver:
            try:
                driver.close()
                driver.quit()
            except WebDriverException:
                pass
        else:
            print("There is no driver!")
