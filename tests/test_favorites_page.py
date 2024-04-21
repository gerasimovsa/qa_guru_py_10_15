import os

import allure
from allure_commons.types import Severity

from ozby_project.data.products import Product
from ozby_project.data.users import User
from ozby_project.model.pages.application import app


@allure.title("Add item to favorites test")
@allure.tag("UI")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "SergeyG")
@allure.feature("Favorites")
@allure.story("Verify that user can add item to favorites")
@allure.link('https://www.oz.by/', name="Main Page")
def test_favorites_add_item():
    user = User(
        email=os.getenv("USER_EMAIL"),
        password=os.getenv("USER_PASSWORD"),
    )
    product = Product(label="Эффективное тестирование")
    app.main_page.open()

    app.main_page.open_authorization_page()
    app.auth_page.authorize_user(user.email, user.password)
    app.main_page.search_item(product.label)
    app.search_result_page.open_item_page(product.label)
    app.item_page.add_current_item_to_favorites()
    app.main_page.open_favorites_page()

    app.favorites_page.should_have_items_added(product.label)

    app.favorites_page.remove_all_items()


@allure.title("Remove item from favorites test")
@allure.tag("UI")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "SergeyG")
@allure.feature("Favorites")
@allure.story("Verify that user can remove item from favorites")
@allure.link('https://www.oz.by/', name="Main Page")
def test_favorites_remove_item():
    user = User(
        email=os.getenv("USER_EMAIL"),
        password=os.getenv("USER_PASSWORD"),
    )
    product = Product(label="Эффективное тестирование")
    app.main_page.open()

    app.main_page.open_authorization_page()
    app.auth_page.authorize_user(user.email, user.password)
    app.main_page.search_item(product.label)
    app.search_result_page.open_item_page(product.label)
    app.item_page.add_current_item_to_favorites()
    app.main_page.open_favorites_page()

    app.favorites_page.remove_all_items()
    app.favorites_page.should_have_all_items_removed_from_favorites()
