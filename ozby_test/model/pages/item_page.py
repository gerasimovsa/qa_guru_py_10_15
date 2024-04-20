from selene import browser, be, have, by, command


class OzItemPage:

    @staticmethod
    def add_current_item_to_cart():
        browser.element(".addtocart-btn").click()
        browser.element("#cart-count").wait_until(be.visible)

    @staticmethod
    def add_current_item_to_favorites():
        browser.element(by.text("В избранное")).click()
        browser.element("#favorite-count").wait_until(be.visible)
