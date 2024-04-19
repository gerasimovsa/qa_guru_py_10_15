from selene import browser, be, have, by, command


class OzAuthorizationPage:
    def __init__(self):
        self.registration_button = browser.element("#loginFormRegisterLink")
        self.phone_submit_registration = browser.element("#registerForm [type='submit']")

        self.email_sign_in_tab_button = browser.element("#loginFormLoginEmailLink")
        self.email_sign_in_submit_button = browser.element("#loginForm [type='submit']")

    def fill_sign_in_form(self, login: str, password: str):
        browser.element("#loginForm [type='email']").should(be.blank).type(login)
        browser.element("#loginForm [type='password']").should(be.blank).type(password)
        return self

    def submit_sign_in_form(self):
        self.email_sign_in_submit_button.click()