from selene import browser, be, have, by, command


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
        browser.element("a[href='/auth/personal.phtml']").click()
        return self

    def open_authorization_page(self):
        browser.element("div.user-bar__item>a").click()
        browser.element("#loginFormLoginEmailLink").click()
        return self

    def open_cart_page(self):
        browser.element(".user-bar__cart").click()
        return self

    def open_favorites_page(self):
        browser.element("a[href='/personal/favorites'].user-bar__item").click()
        return self

    def user_log_out(self):
        browser.element("div.user-bar__item>a[href='/personal/orders/']").should(be.visible).hover()
        browser.element("a[href='/personal']").click()
        browser.element(by.text("Выйти")).click()
        return self

    def search_item(self, query: str):
        browser.element("#top-s").type(query).press_enter()
        return self

    def navigate_to_category(self, top_category: str, middle_category: str, low_category: str, subcategory: str):
        browser.element(by.text(top_category)).click()
        browser.element(f"//span[text()='{middle_category}']/parent::div").click()
        browser.element(by.text(low_category)).click()
        browser.element(by.text(subcategory)).click()
        return self

    def should_have_user_logout(self):
        browser.element("div.user-bar__item>a[href='/personal/orders/']").should(be.not_.visible)
        browser.element("div.user-bar__item>a").should(be.visible)
        return self
