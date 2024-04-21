import allure
from selene import browser, have


class OzCatalogPage:
    def should_have_catalog_path(self, top_category: str, middle_category: str, low_category: str, subcategory: str):
        with allure.step("Checking catalog path"):
            browser.all(".breadcrumbs__list__item>span").should(
                have.exact_texts(["OZ", top_category, middle_category, low_category]))
        with allure.step("Checking opened subcategory"):
            browser.element(".breadcrumbs__list__li>span").should(have.exact_text(subcategory))
        return self
