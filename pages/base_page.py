from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    url_base = "https://magento.softwaretestingboard.com/"
    response = None

    def __init__(self, driver: WebDriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def open_page(self, url):
        self.driver.get(f'{self.url_base}{url}')

    def await_element(self, locator):
        self.wait.until(ec.presence_of_element_located(locator))

    def privacy_policy(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator))
        self.finding_element(*locator).click()

    def finding_element(self, search_type, selector):
        return self.driver.find_element(search_type, selector)

    def finding_elements(self, search_type, selector):
        return self.driver.find_elements(search_type, selector)

    def assert_naming(self, locator: tuple, text):
        self.await_element(locator)
        assert self.finding_element(*locator).text == text, f'Title h1 incorrect {self.finding_element(*locator).text}'
