from test_UI_svs_selenium.pages.base_page import BasePage
from test_UI_svs_selenium.utils.selector_collections_eco_friendly import sort_by, sort_element, all_elements, first_element, second_element
from selenium.webdriver.common.keys import Keys
from typing import Literal


class CollectionsEcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def click_sort(self, sorting_parameter: Literal["Position", "Product Name", "Price"],
                   sort_type: Literal["asc", "desc"]):
        if sort_type == 'asc':
            self.element(*sort_by).send_keys(sorting_parameter, Keys.ENTER)
        elif sort_type == 'desc':
            self.element(*sort_by).send_keys(sorting_parameter, Keys.ENTER)
            self.element(*sort_element).click()
        else:
            return 'Введите тип сортировки "asc" или "desc"'

    def assert_price_after_sort(self, sort_type: Literal["asc", "desc"]):
        self.await_element(all_elements)
        first = self.elements(*all_elements)[0].find_element(*first_element).text.strip('$').split('.')[0]
        second = self.elements(*all_elements)[1].find_element(*second_element).text.strip('$').split('.')[0]
        if sort_type == 'asc':
            assert int(first) < int(second), "do not ascending"
        elif sort_type == 'desc':
            assert int(first) > int(second), "do not descending"
        else:
            return 'Введите тип сортировки "asc" или "desc"'
