from utils.selector_customer_account import error_first_name


def test_create_account_valid_case(customer_account):  # Указать не зарегистрированный email
    customer_account.filling_out_form(firstname='Ted', lastname='Testov', email='tttesttoov@test.com',
                                      password='Qwerty123.', confirm_password='Qwerty123.')
    customer_account.assert_create_message()


def test_existing_email(customer_account):
    customer_account.filling_out_form(firstname='Ted', lastname='Testov', email='test@test.com', password='Qwerty123.',
                                      confirm_password='Qwerty123.')
    customer_account.assert_existing_email()


def test_empty_first_name(customer_account):
    customer_account.filling_out_form(firstname='', lastname='Testov', email='test@test.com', password='Qwerty123.',
                                      confirm_password='Qwerty123.')
    customer_account.assert_error_massege(error_first_name)
