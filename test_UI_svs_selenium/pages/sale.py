from test_UI_svs_selenium.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SalePage(BasePage):
    page_url = '/sale.html'

    def redirect_to_page(self, section):
        menu_section = self.elements(By.XPATH, '//div[@class="categories-menu"]//li')
        for i, row in enumerate(menu_section, start=0):
            if row.text != section:
                continue
            else:
                menu_section[i].find_element(By.CSS_SELECTOR, 'a').click()
                break
