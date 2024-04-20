from selene import browser, be, have, by, command


class OzPersonalDataPage:
    def should_have_user_phone(self, mobile_phone):
        browser.element("input#phone_n").should(have.value("375" + mobile_phone))
        return self

    def should_have_user_data(self, email, first_name, last_name, mobile_phone):
        browser.element("input#email").should(have.value(email))
        browser.element("input[name='first_name']").should(have.value(first_name))
        browser.element("input[name='last_name']").should(have.value(last_name))
        browser.element("input#phone_n").should(have.value("375" + mobile_phone))
        return self

