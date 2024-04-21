import allure
from selene import browser, be


class OzAuthorizationPage:
    def authorize_user(self, email: str, password: str):
        with allure.step("Fill email field"):
            browser.element("#loginForm [type='email']").should(be.blank).type(email)
        with allure.step("Fill password field"):
            browser.element("#loginForm [type='password']").should(be.blank).type(password)
        with allure.step("Submit authorization"):
            browser.element("#loginForm [type='submit']").click()
        return self
