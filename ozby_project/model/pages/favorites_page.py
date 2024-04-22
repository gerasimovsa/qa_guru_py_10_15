import allure
from selene import browser, be, have


class OzFavoritesPage:
    @staticmethod
    def remove_all_items():
        with allure.step("Click on any item's favorite button"):
            for button in browser.all("button.like_active"):
                button.click()
        browser.element("#favorite-count").wait_until(be.not_.visible)

    @staticmethod
    def should_have_items_added(*args):
        with allure.step("Click on any item's favorite button"):
            browser.all(".product-card__title").should(have.texts(args))

    @staticmethod
    def should_have_all_items_removed_from_favorites():
        with allure.step("Check no active favorites buttons"):
            browser.element("button.like_active").should(be.not_.present)
        with allure.step("Check all favorites buttons are toggled off"):
            for element in browser.all("[data-controller='toggle-favorite']"):
                element.should(have.attribute("data-toggle-favorite-is-added-value", "false"))



