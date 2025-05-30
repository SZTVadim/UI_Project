from playwright.sync_api import expect

from test_UI_svs_selenium.pages.base_page import BasePage
from test_UI_svs_selenium.utils.selector_create_account import success_message, error_message_registration, create_button, \
    input_first_name, input_last_name, input_email, input_password, input_confirm_password
from test_UI_svs_selenium.utils.helper import locator_for_error


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    def submit_registration_form(self, firstname=None, lastname=None, email=None, password=None, confirm_password=None):
        self.element(*input_first_name).send_keys(firstname)
        self.element(*input_last_name).send_keys(lastname)
        self.element(*input_email).send_keys(email)
        self.element(*input_password).send_keys(password)
        self.element(*input_confirm_password).send_keys(confirm_password)
        self.click_create_account_button()

    def expect_required_input_error(self, name_input, text):
        locator = locator_for_error(name_input)
        assert locator is not None, f'Name input for {name_input} not found!'
        self.await_element(locator)
        element = self.element(*locator)
        assert element.text == text, f'message is incorrect, your message \n{element().text}'

    def click_create_account_button(self):
        self.element(*create_button).click()

    def expect_account_created_message(self, text):
        # self.await_element(success_message)
        message = self.element(success_message)
        assert message == text

    def expect_email_already_exists(self, text):
        self.await_element(error_message_registration)
        message = self.element(*error_message_registration).text
        expect(message).to_have_text(text)
