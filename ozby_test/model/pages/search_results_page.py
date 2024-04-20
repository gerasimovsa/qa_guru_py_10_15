from selene import browser, be, have, by, command


class OzSearchResultsPage:
    def set_price_range(self, min_price: str, max_price: str):
        browser.element("[name='min']").should(be.blank).type(min_price)
        browser.element("[name='max']").should(be.blank).type(max_price)
        browser.element("span.digi-filters__item").wait_until(be.visible)
        return self

    def enable_search_filter(self, filter_name: str):
        browser.all("span.digi-facet-option__text").element_by(have.text(filter_name)).perform(
            command.js.scroll_into_view).click()
        return self

    def open_item_page(self, item: str):
        browser.element(by.partial_text(item)).click()
        return self

    def should_have_search_results(self, product_quantity: str = None, product_labels: list[str] = None):
        if product_quantity:
            browser.element("span.digi-products__quantity").should(have.exact_text(product_quantity))
        if product_labels:
            browser.all("a.digi-product__label").should(have.exact_texts(product_labels))
        return self

    def should_have_filters_active(self, *args):
        browser.all("span.digi-filters__item-value").should(have.texts(args))
        return self
