from ozby_project.model.pages.authorization_page import OzAuthorizationPage
from ozby_project.model.pages.cart_page import OzCartPage
from ozby_project.model.pages.catalog_page import OzCatalogPage
from ozby_project.model.pages.favorites_page import OzFavoritesPage
from ozby_project.model.pages.item_page import OzItemPage
from ozby_project.model.pages.main_page import OzMainPage
from ozby_project.model.pages.personal_data_page import OzPersonalDataPage
from ozby_project.model.pages.registration_page import OzRegistrationPage
from ozby_project.model.pages.search_results_page import OzSearchResultsPage


class Application:
    def __init__(self):
        self.main_page = OzMainPage()
        self.registration_page = OzRegistrationPage()
        self.auth_page = OzAuthorizationPage()
        self.personal_data_page = OzPersonalDataPage()
        self.search_result_page = OzSearchResultsPage()
        self.catalog_page = OzCatalogPage()
        self.cart_page = OzCartPage()
        self.item_page = OzItemPage()
        self.favorites_page = OzFavoritesPage()


app = Application()


