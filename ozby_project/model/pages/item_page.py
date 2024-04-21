import allure
from selene import browser, be, by


class OzItemPage:

    def add_current_item_to_cart(self):
        with allure.step("Click on add to cart button"):
            browser.element(".addtocart-btn").click()
        with allure.step("Wait until item count in cart is updated"):
            browser.element("#cart-count").wait_until(be.visible)
        return self

    def add_current_item_to_favorites(self):
        with allure.step("Click on add to favorite button"):
            browser.element(by.text("В избранное")).click()
        with allure.step("Wait until item count in favorites is updated"):
            browser.element("#favorite-count").wait_until(be.visible)
        return self
