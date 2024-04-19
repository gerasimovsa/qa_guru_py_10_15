from selene import browser, be, have, by, command

from model.pages.authorization_page import OzAuthorizationPage
from model.pages.main_page import OzMainPage
from model.pages.personal_data_page import OzPersonalDataPage
from model.pages.registration_page import OzRegistrationPage


def test_phone_register():
    main_page = OzMainPage()
    registration_page = OzRegistrationPage()
    personal_data_page = OzPersonalDataPage()

    main_page.open()
    main_page.open_registration_page()
    registration_page.fill_registration_phone("445821620")
    registration_page.submit_registration_and_enter()
    main_page.open_personal_data_page()
    personal_data_page.should_have_user_phone("445821620")


def test_email_authorization():
    browser.open("/")
    browser.element("div.user-bar__item>a").click()
    browser.element("#loginFormLoginEmailLink").click()
    browser.element("#loginForm [type='email']").should(be.blank).type("test_oz_001@gmail.com")
    browser.element("#loginForm [type='password']").should(be.blank).type("h34Duz")
    browser.element("#loginForm [type='submit']").click()
    browser.element("div.user-bar__item>a[href='/personal/orders/']").should(be.visible).hover()
    browser.element("a[href='/personal']").click()
    browser.element(".l-row-user-name h1").should(have.exact_text("oz_test"))
    browser.element(".l-row-user-name p").should(have.exact_text("User Test"))


def test_log_out():
    pass


def test_search_items():
    browser.open("/")
    browser.element("#top-s").type("Django").press_enter()
    browser.element("span.digi-products__quantity").should(have.exact_text("5"))
    browser.all("a.digi-product__label").should(have.exact_texts(
        ["Django 3.0. Практика создания веб-сайтов на Python",
         "Python, Django и Bootstrap для начинающих",
         "Django 2 в примерах",
         "Django 4. Практика создания веб-сайтов на Python",
         "Python, Django и PyCharm для начинающих"]
    ))


def test_filter_search_result():
    browser.open("/")
    browser.element("#top-s").should(be.blank).type("Python").press_enter()
    browser.element("[name='max']").should(be.blank).type("30")
    browser.element("span.digi-filters__item").wait_until(be.visible)
    browser.all("span.digi-facet-option__text").element_by(have.text("BHV")).perform(
        command.js.scroll_into_view).click()
    browser.all("span.digi-facet-option__text").element_by(have.text("2023")).perform(
        command.js.scroll_into_view).click()
    browser.all("span.digi-filters__item-value").should(have.texts(["0 - 30", "BHV", "2023"]))
    browser.element("a.digi-product__label").should(have.exact_text("Python. 12 уроков для начинающих"))


def test_navigate_catalog():
    browser.open("/")
    browser.element(by.text("Книги")).click()
    browser.element("//span[text()='Нехудожественная литература']/parent::div").click()
    browser.element(by.text("Компьютеры и Интернет")).click()
    browser.element(by.text("Книги про компьютерные игры")).click()
    browser.all(".breadcrumbs__list__item>span").should(
        have.exact_texts(["OZ", "Книги", "Нехудожественная литература", "Компьютеры и Интернет"]))
    browser.element(".breadcrumbs__list__li>span").should(have.exact_text("Книги про компьютерные игры"))


def test_cart_add_item():
    browser.open("/")
    browser.element("div.user-bar__item>a").click()
    browser.element("#loginFormLoginEmailLink").click()
    browser.element("#loginForm [type='email']").should(be.blank).type("test_oz_001@gmail.com")
    browser.element("#loginForm [type='password']").should(be.blank).type("h34Duz")
    browser.element("#loginForm [type='submit']").click()

    browser.element("#top-s").type("Эффективное тестирование")
    browser.element(by.partial_text("Эффективное тестирование")).click()
    browser.element(".addtocart-btn").click()

    browser.element(".user-bar__cart").click()
    browser.element(".goods-table-cell__line_title").should(
        have.text("Эффективное тестирование программного обеспечения"))
    browser.element(".deal-form").should(be.present)


def test_cart_remove_item():
    browser.open("/")
    browser.element("div.user-bar__item>a").click()
    browser.element("#loginFormLoginEmailLink").click()
    browser.element("#loginForm [type='email']").should(be.blank).type("test_oz_001@gmail.com")
    browser.element("#loginForm [type='password']").should(be.blank).type("h34Duz")
    browser.element("#loginForm [type='submit']").click()

    browser.element("#top-s").type("Эффективное тестирование")
    browser.element(by.partial_text("Эффективное тестирование")).click()
    browser.element(".addtocart-btn").click()

    browser.element(".user-bar__cart").click()
    browser.element(".checkAll").click()
    browser.element("button.remove").click()
    browser.element("button.remove-yes").click()

    browser.element(".goods-table-cell__line_title").should(be.not_.present)
    browser.element(".deal-form").should(be.not_.present)


def test_favorites_add_item():
    browser.open("/")
    browser.element("div.user-bar__item>a").click()
    browser.element("#loginFormLoginEmailLink").click()
    browser.element("#loginForm [type='email']").should(be.blank).type("test_oz_001@gmail.com")
    browser.element("#loginForm [type='password']").should(be.blank).type("h34Duz")
    browser.element("#loginForm [type='submit']").click()

    browser.element("#top-s").type("Эффективное тестирование")
    browser.element(by.partial_text("Эффективное тестирование")).click()
    browser.element(by.text("В избранное")).click()

    browser.element(by.text("Избранное")).click()

    browser.element(".product-card__title").should(have.text("Эффективное тестирование программного обеспечения"))


def test_favorites_remove_item():
    browser.open("/")
    browser.element("div.user-bar__item>a").click()
    browser.element("#loginFormLoginEmailLink").click()
    browser.element("#loginForm [type='email']").should(be.blank).type("test_oz_001@gmail.com")
    browser.element("#loginForm [type='password']").should(be.blank).type("h34Duz")
    browser.element("#loginForm [type='submit']").click()

    browser.element("#top-s").type("Эффективное тестирование")
    browser.element(by.partial_text("Эффективное тестирование")).click()
    browser.element(by.text("В избранное")).click()

    browser.element(by.text("Избранное")).click()

    browser.element("button.like_active").click()
    browser.element("button.like_active").should(be.not_.present)
    browser.element("[data-controller='toggle-favorite']").should(
        have.attribute("data-toggle-favorite-is-added-value", "false"))
