from selenium.webdriver.common.by import By

create_button = (By.CSS_SELECTOR, '.action.submit')
input_first_name = (By.ID, 'firstname')
input_last_name = (By.ID, 'lastname')
input_email = (By.ID, 'email_address')
input_password = (By.ID, 'password')
input_confirm_password = (By.ID, 'password-confirmation')
success_message = (By.CSS_SELECTOR, '.message-success')

error_first_name = (By.ID, 'firstname-error')
error_last_name = (By.ID, 'lastname-error')
error_email = (By.ID, 'email_address-error')
error_password = (By.ID, 'password-error')
error_confirm_password = (By.ID, 'password-confirmation-error')
error_message_registration = (By.CSS_SELECTOR, '.page.messages')
