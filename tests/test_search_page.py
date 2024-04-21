import allure
from allure_commons.types import Severity

from ozby_project.data.products import Product
from ozby_project.model.pages.application import app


@allure.title("Search item test")
@allure.tag("UI")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "SergeyG")
@allure.feature("Search bar")
@allure.story("Verify that user can search for items using header search bar")
@allure.link('https://www.oz.by/', name="Main Page")
def test_search_items():
    product = Product(
        label="Django",
        quantity=5,
        items=['Django 3.0. Практика создания веб-сайтов на Python',
               'Django 2 в примерах',
               'Python, Django и Bootstrap для начинающих',
               'Django 4. Практика создания веб-сайтов на Python',
               'Python, Django и PyCharm для начинающих']
    )
    app.main_page.open()

    app.main_page.search_item(product.label)

    app.search_result_page.should_have_search_results(product.quantity, product.items)


@allure.title("Filter search results test")
@allure.tag("UI")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "SergeyG")
@allure.feature("Search result filters")
@allure.story("Verify that user can filter search results")
@allure.link('https://www.oz.by/', name="Main Page")
def test_filter_search_result():
    product = Product(
        label="Python",
        items=["Python. 12 уроков для начинающих"]
    )
    app.main_page.open()

    app.main_page.search_item(product.label)
    app.search_result_page.set_price_range("0", "30")
    app.search_result_page.enable_search_filter("BHV")
    app.search_result_page.enable_search_filter("2023")

    app.search_result_page.should_have_filters_active("0 - 30", "BHV", "2023")
    app.search_result_page.should_have_search_results(product_labels=product.items)
