from pages.base_page import BasePage
from utils.selector_customer_account import create_button, input_first_name, input_last_name, input_email, \
    input_password, input_confirm_password, success_message, error_message_registration


class CustomerAccount(BasePage):
    page_url = '/customer/account/create/'

    def filling_out_form(self, firstname, lastname, email, password, confirm_password):
        self.finding_element(*input_first_name).send_keys(firstname)
        self.finding_element(*input_last_name).send_keys(lastname)
        self.finding_element(*input_email).send_keys(email)
        self.finding_element(*input_password).send_keys(password)
        self.finding_element(*input_confirm_password).send_keys(confirm_password)
        self.click_create_button()

    def assert_error_massege(self, selector_error):
        self.await_element(selector_error)
        element = self.finding_element(*selector_error)
        assert element.text == 'This is a required field.', f'message is incorrect, your message \n{element.text}'

    def click_create_button(self):
        self.finding_element(*create_button).click()

    def assert_create_message(self):
        self.await_element(success_message)
        message = self.finding_element(*success_message).text
        assert message == 'Thank you for registering with Main Website Store.'

    def assert_existing_email(self):
        self.await_element(error_message_registration)
        message = self.finding_element(*error_message_registration).text
        assert message == (
            'There is already an account with this email address. '
            'If you are sure that it is your email address, '
            'click here to get your password and access your account.'), f'твое сообщение: \n{message}'

    # def data_verification(self):
    #     assert data
