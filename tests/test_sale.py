from utils.selector_sale import title_h_1, menu_sale
from utils.selector_jackets_women import title_h_1 as h1_jackets


def test_header_h_1(sale_page):
    sale_page.assert_naming(title_h_1, 'Sale')  # проверяем корректность заголовка h1


def test_menu_sale(sale_page):
    sale_page.assert_naming(menu_sale, 'Sale')  # проверяем что находимся в меню Sale


def test_redirect_from_menu(sale_page):
    sale_page.redirect_any_page('Jackets')
    sale_page.assert_naming(h1_jackets, 'Jackets')
