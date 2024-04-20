from selene import browser, be, have, by, command


class OzRegistrationPage:

    @staticmethod
    def phone_register_and_enter(value: str):
        browser.element("#registerForm [type='tel']").click().type(value)
        browser.element("#registerForm [type='submit']").click()
        browser.element("button[value='pp']").click()
