import allure
from selene import browser


class OzRegistrationPage:
    def phone_register_and_enter(self, value: str):
        with allure.step("Fill phone field"):
            browser.element("#registerForm [type='tel']").click().type(value)
        with allure.step("Submit registration"):
            browser.element("#registerForm [type='submit']").click()
        with allure.step("Accept data privacy terms"):
            browser.element("button[value='pp']").click()
        return self
