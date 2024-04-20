from ozby_test.model.pages.cart_page import OzCartPage
from ozby_test.model.pages.catalog_page import OzCatalogPage
from ozby_test.model.pages import OzFavoritesPage
from ozby_test.model.pages.item_page import OzItemPage
from ozby_test.model.pages.main_page import OzMainPage
from ozby_test.model.pages.personal_data_page import OzPersonalDataPage
from ozby_test.model.pages.authorization_page import OzAuthorizationPage
from ozby_test.model.pages import OzRegistrationPage
from ozby_test.model.pages import OzSearchResultsPage


def test_phone_registration():
    main_page = OzMainPage()
    registration_page = OzRegistrationPage()
    personal_data_page = OzPersonalDataPage()
    main_page.open()

    main_page.open_registration_page()
    registration_page.phone_register_and_enter("445821620")
    main_page.open_personal_data_page()

    personal_data_page.should_have_user_phone("445821620")


def test_email_authorization():
    main_page = OzMainPage()
    auth_page = OzAuthorizationPage()
    personal_data_page = OzPersonalDataPage()
    main_page.open()

    main_page.open_authorization_page()
    auth_page.authorize_user("test_oz_001@gmail.com", "h34Duz")
    main_page.open_personal_data_page()

    personal_data_page.should_have_user_data(
        "test_oz_001@gmail.com",
        "User",
        "Test",
        "443322111"
    )


def test_log_out():
    main_page = OzMainPage()
    auth_page = OzAuthorizationPage()
    main_page.open()

    main_page.open_authorization_page()
    auth_page.authorize_user("test_oz_001@gmail.com", "h34Duz")
    main_page.user_log_out()

    main_page.should_have_user_logout()


def test_search_items():
    main_page = OzMainPage()
    search_result_page = OzSearchResultsPage()
    main_page.open()

    main_page.search_item("Django")
    search_result_page.should_have_search_results("5",
                                                  ['Django 3.0. Практика создания веб-сайтов на Python',
                                                   'Django 2 в примерах',
                                                   'Python, Django и Bootstrap для начинающих',
                                                   'Django 4. Практика создания веб-сайтов на Python',
                                                   'Python, Django и PyCharm для начинающих'])


def test_filter_search_result():
    main_page = OzMainPage()
    search_result_page = OzSearchResultsPage()
    main_page.open()

    main_page.search_item("Python")
    search_result_page.set_price_range("0", "30")
    search_result_page.enable_search_filter("BHV")
    search_result_page.enable_search_filter("2023")

    search_result_page.should_have_filters_active("0 - 30", "BHV", "2023")
    search_result_page.should_have_search_results(product_labels=["Python. 12 уроков для начинающих"])


def test_navigate_catalog():
    main_page = OzMainPage()
    catalog_page = OzCatalogPage()
    main_page.open()

    main_page.navigate_to_category("Книги",
                                   "Нехудожественная литература",
                                   "Компьютеры и Интернет",
                                   "Книги про компьютерные игры")
    catalog_page.should_have_catalog_path("Книги",
                                          "Нехудожественная литература",
                                          "Компьютеры и Интернет",
                                          "Книги про компьютерные игры")


def test_cart_add_item():
    main_page = OzMainPage()
    auth_page = OzAuthorizationPage()
    search_results_page = OzSearchResultsPage()
    cart_page = OzCartPage()
    item_page = OzItemPage()
    main_page.open()

    main_page.open_authorization_page()
    auth_page.authorize_user("test_oz_001@gmail.com", "h34Duz")
    main_page.search_item("Эффективное тестирование")
    search_results_page.open_item_page("Эффективное тестирование")
    item_page.add_current_item_to_favorites()

    main_page.open_cart_page()
    cart_page.should_have_items_added("Эффективное тестирование")

    cart_page.remove_all_items()


def test_cart_remove_item():
    main_page = OzMainPage()
    auth_page = OzAuthorizationPage()
    search_results_page = OzSearchResultsPage()
    cart_page = OzCartPage()
    item_page = OzItemPage()
    main_page.open()

    main_page.open_authorization_page()
    auth_page.authorize_user("test_oz_001@gmail.com", "h34Duz")
    main_page.search_item("Эффективное тестирование")
    search_results_page.open_item_page("Эффективное тестирование")
    item_page.add_current_item_to_favorites()

    main_page.open_cart_page()
    cart_page.should_have_items_added("Эффективное тестирование")
    cart_page.remove_all_items()
    cart_page.should_be_empty()


def test_favorites_add_item():
    main_page = OzMainPage()
    auth_page = OzAuthorizationPage()
    search_results_page = OzSearchResultsPage()
    favorites_page = OzFavoritesPage()
    item_page = OzItemPage()
    main_page.open()

    main_page.open_authorization_page()
    auth_page.authorize_user("test_oz_001@gmail.com", "h34Duz")
    main_page.search_item("Эффективное тестирование")
    search_results_page.open_item_page("Эффективное тестирование")
    item_page.add_current_item_to_favorites()
    main_page.open_favorites_page()

    favorites_page.should_have_items_added("Эффективное тестирование")

    favorites_page.remove_all_items()


def test_favorites_remove_item():
    main_page = OzMainPage()
    auth_page = OzAuthorizationPage()
    search_results_page = OzSearchResultsPage()
    favorites_page = OzFavoritesPage()
    item_page = OzItemPage()
    main_page.open()

    main_page.open_authorization_page()
    auth_page.authorize_user("test_oz_001@gmail.com", "h34Duz")
    main_page.search_item("Эффективное тестирование")
    search_results_page.open_item_page("Эффективное тестирование")
    item_page.add_current_item_to_favorites()
    main_page.open_favorites_page()

    favorites_page.remove_all_items()
    favorites_page.should_have_all_items_removed_from_favorites()
