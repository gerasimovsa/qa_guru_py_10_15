from selene import browser, be, have, by, command


class OzRegistrationPage:
    def __init__(self):
        self.registration_button = browser.element("#loginFormRegisterLink")
        self.phone_submit_registration = browser.element("#registerForm [type='submit']")

        self.email_sign_in_tab_button = browser.element("#loginFormLoginEmailLink")
        self.email_sign_in_submit_button = browser.element("#loginForm [type='submit']")

    def fill_registration_phone(self, value: str):
        browser.element("#registerForm [type='tel']").click().type(value)
        return self

    def submit_registration_and_enter(self):
        browser.element("#registerForm [type='submit']").click()
        browser.element("#registerForm [type='submit']").click()
        return self
