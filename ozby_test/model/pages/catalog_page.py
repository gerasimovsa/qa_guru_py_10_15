from selene import browser, be, have, by, command


class OzCatalogPage:
    def should_have_catalog_path(self, top_category: str, middle_category: str, low_category: str, subcategory: str):
        browser.all(".breadcrumbs__list__item>span").should(
            have.exact_texts(["OZ", top_category, middle_category, low_category]))
        browser.element(".breadcrumbs__list__li>span").should(have.exact_text(subcategory))
        return self
