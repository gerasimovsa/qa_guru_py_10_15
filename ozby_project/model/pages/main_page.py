import allure
from selene import browser, be, by


class OzMainPage:

    def open(self):
        with allure.step("Open https://oz.by page"):
            browser.open("/")
        return self

    def open_registration_page(self):
        with allure.step("Click on sign in button"):
            browser.element("div.user-bar__item>a").click()
        with allure.step("Click on register button"):
            browser.element("#loginFormRegisterLink").click()
        return self

    def open_personal_data_page(self):
        with allure.step("Hover over personal menu"):
            browser.element("div.user-bar__item>a[href='/personal/orders/']").should(be.visible).hover()
        with allure.step("Click on personal button"):
            browser.element("a[href='/personal']").click()
        with allure.step("Click on personal data button"):
            browser.element("a[href='/auth/personal.phtml']").click()
        return self

    def open_authorization_page(self):
        with allure.step("Click on sign in button"):
            browser.element("div.user-bar__item>a").click()
        with allure.step("Select login with email tab"):
            browser.element("#loginFormLoginEmailLink").click()
        return self

    def open_cart_page(self):
        with allure.step("Click on cart button"):
            browser.element(".user-bar__cart").click()
        return self

    def open_favorites_page(self):
        with allure.step("Click on favorites button"):
            browser.element("a[href='/personal/favorites'].user-bar__item").click()
        return self

    def user_log_out(self):
        with allure.step("Hover over personal menu"):
            browser.element("div.user-bar__item>a[href='/personal/orders/']").should(be.visible).hover()
        with allure.step("Click on personal button"):
            browser.element("a[href='/personal']").click()
        with allure.step("Click on exit button"):
            browser.element(by.text("Выйти")).click()
        return self

    def search_item(self, query: str):
        with allure.step(f"Enter {query} into search bar"):
            browser.element("#top-s").type(query).press_enter()
        return self

    def navigate_to_category(self, top_category: str, middle_category: str, low_category: str, subcategory: str):
        with allure.step(f"Got to {top_category} category"):
            browser.element(by.text(top_category)).click()
        with allure.step(f"Got to {middle_category} category"):
            browser.element(f"//span[text()='{middle_category}']/parent::div").click()
        with allure.step(f"Go to {low_category} category"):
            browser.element(by.text(low_category)).click()
        with allure.step(f"Go to {subcategory} subcategory"):
            browser.element(by.text(subcategory)).click()
        return self

    def should_have_user_logout(self):
        with allure.step("Check orders menu is not present"):
            browser.element("div.user-bar__item>a[href='/personal/orders/']").should(be.not_.visible)
        with allure.step("Check personal menu is not present"):
            browser.element("div.user-bar__item>a").should(be.visible)
        return self
