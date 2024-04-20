from selene import browser, be, have, by, command


class OzCartPage:
    @staticmethod
    def remove_all_items():
        browser.element(".checkAll").click()
        browser.element("button.remove").click()
        browser.element("button.remove-yes").click()

    @staticmethod
    def should_have_items_added(*args):
        browser.all(".goods-table-cell__line_title").should(have.texts(args))
        browser.element(".deal-form").should(be.present)

    @staticmethod
    def should_be_empty():
        browser.element(".goods-table-cell__line_title").should(be.not_.present)
        browser.element(".deal-form").should(be.not_.present)
