import utils.selector_create_account as locator

text_email_already_exists = ('There is already an account with this email address. '
                             'If you are sure that it is your email address, '
                             'click here to get your password and access your account.')
text_required_input_error = 'This is a required field.'
text_account_created_message = 'Thank you for registering with Main Website Store.'


def locator_for_error(key):
    return getattr(locator, f'error_{key}', None)
