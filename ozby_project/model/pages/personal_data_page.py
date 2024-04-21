import allure
from selene import browser, have


class OzPersonalDataPage:
    def should_have_user_phone(self, mobile_phone):
        with allure.step("Check phone field"):
            browser.element("input#phone_n").should(have.value("375" + mobile_phone))
        return self

    def should_have_user_data(self, email, first_name, last_name, mobile_phone):
        with allure.step("Check email field"):
            browser.element("input#email").should(have.value(email))
        with allure.step("Check first name field"):
            browser.element("input[name='first_name']").should(have.value(first_name))
        with allure.step("Check last name field"):
            browser.element("input[name='last_name']").should(have.value(last_name))
        with allure.step("Check phone field"):
            browser.element("input#phone_n").should(have.value("375" + mobile_phone))
        return self
