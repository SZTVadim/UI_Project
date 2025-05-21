from pages.base_page import BasePage
from utils.selector_collections_eco_friendly import sort_by, sort_element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class CollectionsEcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def sorted_price_asc(self):  # по дефолту asc ⬆
        self.finding_element(*sort_by).send_keys('Price', Keys.ENTER)

    def sorted_price_desc(self):  # сортировка desc
        self.finding_element(*sort_by).send_keys('Price', Keys.ENTER)
        self.finding_element(*sort_element).click()

    def assert_price_elements_asc(self, all_elements, first_element, second_element):
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.column.main')))
        first = self.finding_elements(*all_elements)[0].find_element(*first_element).text.strip('$').split('.')[0]
        second = self.finding_elements(*all_elements)[1].find_element(*second_element).text.strip('$').split('.')[0]
        assert int(first) < int(second), "do not ascending"

    def assert_price_elements_desc(self, all_elements, first_element, second_element):
        self.await_element(all_elements)
        first = self.finding_elements(*all_elements)[0].find_element(*first_element).text.strip('$').split('.')[0]
        second = self.finding_elements(*all_elements)[1].find_element(*second_element).text.strip('$').split('.')[0]
        assert int(first) > int(second), "do not ascending"
