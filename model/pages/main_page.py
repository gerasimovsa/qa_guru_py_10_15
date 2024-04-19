from selene import browser, be, have, by, command

from model.pages import resource


class OzMainPage:

    def open(self):
        browser.open("/")
        return self

    def open_registration_page(self):
        browser.element("div.user-bar__item>a").click()
        browser.element("#loginFormRegisterLink").click()
        return self

    def open_personal_data_page(self):
        browser.element("div.user-bar__item>a[href='/personal/orders/']").should(be.visible).hover()
        browser.element("a[href='/personal']").click()
        browser.element("href='/auth/personal.phtml']").click()
        return self
