import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.customer_account import CustomerAccount
from pages.collections_eco_friendly import CollectionsEcoFriendly
from pages.sale import SalePage
from utils.selector_base_page import disagree_btn


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver=driver, timeout=15)
    return wait


@pytest.fixture()
def driver():
    driver = WebDriver()
    driver.maximize_window()
    yield driver


@pytest.fixture()
def customer_account(driver, wait):
    page = CustomerAccount(driver, wait)
    page.open_page()
    page.privacy_policy(disagree_btn)
    yield page
    driver.quit()


@pytest.fixture()
def eco_friendly(driver, wait):
    page = CollectionsEcoFriendly(driver, wait)
    page.open_page()
    page.privacy_policy(disagree_btn)
    yield page
    driver.quit()


@pytest.fixture()
def sale_page(driver, wait):
    page = SalePage(driver, wait)
    page.open_page()
    page.privacy_policy(disagree_btn)
    yield page
    driver.quit()
