from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.selector_base_page import disagree_btn, title_h1
from utils.selector_sale import menu_sale


class BasePage:
    url_base = "https://magento.softwaretestingboard.com/"
    response = None
    page_url = None

    def __init__(self, driver: WebDriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def open_page(self):
        self.driver.get(f'{self.url_base}{self.page_url}')

    def first_page_open(self):
        self.driver.get(f'{self.url_base}{self.page_url}')
        self.await_element(disagree_btn)
        self.close_cookie_banner()

    def await_element(self, locator):
        self.wait.until(ec.presence_of_element_located(locator))

    def close_cookie_banner(self):
        self.wait.until(ec.element_to_be_clickable(disagree_btn))
        self.element(*disagree_btn).click()

    def element(self, search_type, selector):
        return self.driver.find_element(search_type, selector)

    def elements(self, search_type, selector):
        return self.driver.find_elements(search_type, selector)

    def check_that_page_title_is(self, text):
        self.await_element(title_h1)
        assert self.element(*title_h1).text == text, f'Title h1 incorrect, your title is {self.element(*title_h1).text}'

    def check_current_menu_section(self, text):
        self.await_element(menu_sale)
        assert self.element(*menu_sale).text == text, ('Title menu incorrect, '
                                                       f'your title is {self.element(*menu_sale).text}')
