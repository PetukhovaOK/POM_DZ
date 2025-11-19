from data.credentials import Credentials
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.your_cart_page import YourCartPage
from pages.chechout_your_information_page import ChechoutYourInformationPage
from pages.chechout_overview_page import ChechoutOverviewPage
from pages.chechout_complete_page import ChechoutCompletePage



class BaseTest:

    def setup_method(self):
        self.credentials = Credentials()
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.your_cart_page = YourCartPage(self.driver)
        self.chechout_your_information_page = ChechoutYourInformationPage(self.driver)
        self.chechout_overview_page = ChechoutOverviewPage(self.driver)
        self.chechout_complete_page = ChechoutCompletePage(self.driver)


