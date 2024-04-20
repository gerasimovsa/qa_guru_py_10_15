from selene import browser, be, have, by, command


class OzAuthorizationPage:
    def authorize_user(self, email: str, password: str):
        browser.element("#loginForm [type='email']").should(be.blank).type(email)  # test_oz_001@gmail.com
        browser.element("#loginForm [type='password']").should(be.blank).type(password)  # h34Duz
        browser.element("#loginForm [type='submit']").click()
        return self
