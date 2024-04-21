import os

import allure
import pytest
from allure_commons.types import Severity

from ozby_project.data.products import Product
from ozby_project.data.users import User
from ozby_project.model.pages.application import app


@allure.title("User registration test")
@allure.tag("UI")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SergeyG")
@allure.feature("Registration")
@allure.story("Verify that user can register using a phone number")
@allure.link('https://www.oz.by/', name="Main Page")
@pytest.mark.skip
def test_phone_registration():
    user = User(
        mobile_phone=os.getenv("UNREGISTERED_USER_PHONE")
    )
    app.main_page.open()

    app.main_page.open_registration_page()
    app.registration_page.phone_register_and_enter(user.mobile_phone)
    app.main_page.open_personal_data_page()

    app.personal_data_page.should_have_user_phone(user.mobile_phone)


@allure.title("User authorization test")
@allure.tag("UI")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SergeyG")
@allure.feature("Authorization")
@allure.story("Verify that user can authorize using credentials")
@allure.link('https://www.oz.by/', name="Main Page")
def test_email_authorization():
    user = User(
        email=os.getenv("USER_EMAIL"),
        password=os.getenv("USER_PASSWORD"),
        mobile_phone=os.getenv("USER_PHONE"),
        first_name="User",
        last_name="Test"
    )
    app.main_page.open()

    app.main_page.open_authorization_page()
    app.auth_page.authorize_user(user.email, user.password)
    app.main_page.open_personal_data_page()

    app.personal_data_page.should_have_user_data(
        user.email,
        user.first_name,
        user.last_name,
        user.mobile_phone
    )


@allure.title("User logout test")
@allure.tag("UI")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SergeyG")
@allure.feature("Log out")
@allure.story("Verify that user log out")
@allure.link('https://www.oz.by/', name="Main Page")
def test_log_out():
    user = User(
        email=os.getenv("USER_EMAIL"),
        password=os.getenv("USER_PASSWORD")
    )
    app.main_page.open()

    app.main_page.open_authorization_page()
    app.auth_page.authorize_user(user.email, user.password)
    app.main_page.user_log_out()

    app.main_page.should_have_user_logout()


@allure.title("Navigate in catalog test")
@allure.tag("UI")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "SergeyG")
@allure.feature("Catalog")
@allure.story("Verify that user can navigate to subcategory in catalog")
@allure.link('https://www.oz.by/', name="Main Page")
def test_navigate_catalog():
    product = Product(
        categories=[
            "Книги",
            "Нехудожественная литература",
            "Компьютеры и Интернет",
            "Книги про компьютерные игры"
        ]
    )
    app.main_page.open()

    app.main_page.navigate_to_category(*product.categories)
    app.catalog_page.should_have_catalog_path(*product.categories)
