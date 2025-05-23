def test_assert_header_h1(eco_friendly):
    eco_friendly.first_page_open()
    eco_friendly.check_that_page_title_is('Eco Friendly')  # проверяем корректность заголовка h1


def test_sort_asc(eco_friendly):
    eco_friendly.first_page_open()
    eco_friendly.click_sort('Price', 'asc')  # проверка сортировки asc (явно бага на сайте, там она как desc указана)
    eco_friendly.assert_price_after_sort(sort_type='asc')


def test_sort_desc(eco_friendly):
    eco_friendly.first_page_open()
    eco_friendly.click_sort('Price', 'desc')  # проверка сортировки desc
    eco_friendly.assert_price_after_sort(sort_type='desc')
