import allure
from selene import browser, be, have


class OzCartPage:
    def remove_all_items(self):
        with allure.step("Select all items in cart"):
            browser.element(".checkAll").click()
        with allure.step("Remove items"):
            browser.element("button.remove").click()
        with allure.step("Confirm remove"):
            browser.element("button.remove-yes").click()
        return self

    def should_have_items_added(self, *args):
        with allure.step("Check product labels in cart"):
            browser.all(".goods-table-cell__line_title").should(have.texts(args))
        with allure.step("Check checkout menu is available"):
            browser.element(".deal-form").should(be.present)
        return self

    def should_be_empty(self):
        with allure.step("Check cart is empty"):
            browser.element(".goods-table-cell__line_title").should(be.not_.present)
        with allure.step("Check checkout menu is not available"):
            browser.element(".deal-form").should(be.not_.present)
        return self
