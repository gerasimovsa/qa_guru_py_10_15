from selene import browser, be, have, by, command
from utils.format_data import format_phone_number


class OzPersonalDataPage:

    @staticmethod
    def should_have_user_phone(mobile_number):
        formatted_phone = format_phone_number(mobile_number)
        browser.element("input#phone_n").should(have.value(formatted_phone))

    @staticmethod
    def should_have_user_data(email, first_name, last_name, mobile_phone):
        browser.element("input#email").should(have.value(email))
        browser.element("input[name='first_name']").should(have.value(first_name))
        browser.element("input[name='last_name']").should(have.value(last_name))
        formatted_phone = format_phone_number(mobile_phone)
        browser.element("input#phone_n").should(have.value(formatted_phone))
