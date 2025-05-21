from utils.selector_collections_eco_friendly import title_h_1, all_elements, first_element, second_element


def test_header_h_1(eco_friendly):
    eco_friendly.open_page(url=eco_friendly.page_url)
    eco_friendly.assert_naming(title_h_1, 'Eco Friendly')  # проверяем корректность заголовка h1


def test_sort_asc(eco_friendly):
    eco_friendly.open_page(url=eco_friendly.page_url)
    eco_friendly.sorted_price_asc()  # проверка сортировки asc (явно бага на сайте, там она как desc указана)
    eco_friendly.assert_price_elements_asc(all_elements, first_element, second_element)


def test_sort_desc(eco_friendly):
    eco_friendly.open_page(url=eco_friendly.page_url)
    eco_friendly.sorted_price_desc()  # проверка сортировки desc
    eco_friendly.assert_price_elements_desc(all_elements, first_element, second_element)
