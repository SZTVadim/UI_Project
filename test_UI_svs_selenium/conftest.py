import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from test_UI_svs_pw.pages.create_account import CreateAccount
from test_UI_svs_pw.pages.collections_eco_friendly import CollectionsEcoFriendly
from test_UI_svs_pw.pages.jackets_women import JacketsWomen
from test_UI_svs_pw.pages.sale import SalePage


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver=driver, timeout=20)
    return wait


@pytest.fixture()
def driver():
    driver = WebDriver()
    driver.maximize_window()
    yield driver


@pytest.fixture()
def register_page(driver, wait):
    page = CreateAccount(driver, wait)
    yield page
    driver.quit()


@pytest.fixture()
def eco_friendly_page(driver, wait):
    page = CollectionsEcoFriendly(driver, wait)
    yield page
    driver.quit()


@pytest.fixture()
def sale_page(driver, wait):
    page = SalePage(driver, wait)
    yield page
    driver.quit()


@pytest.fixture()
def jackets_women_page(driver, wait):
    page = JacketsWomen(driver, wait)
    yield page
    driver.quit()
