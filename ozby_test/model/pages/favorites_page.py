from selene import browser, be, have, by, command


class OzFavoritesPage:
    @staticmethod
    def remove_all_items():
        for button in browser.all("button.like_active"):
            button.click()

    @staticmethod
    def should_have_items_added(*args):
        browser.all(".product-card__title").should(have.texts(args))

    @staticmethod
    def should_have_all_items_removed_from_favorites():
        browser.element("button.like_active").should(be.not_.present)
        for element in browser.all("[data-controller='toggle-favorite']"):
            element.should(have.attribute("data-toggle-favorite-is-added-value", "false"))



