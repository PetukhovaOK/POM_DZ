from base.base_page import BasePage
from data.urls import Urls
from selenium.webdriver.support import expected_conditions as EC

class YourCartPage(BasePage):

    _PAGE_URL = Urls.YOUR_CART_PAGE

    _CHECKOUT_BUTTON = "//button[@id='checkout']"

    # нажимаем кнопку Checkout
    def chechout_button(self):
        self.wait.until(EC.element_to_be_clickable(self._CHECKOUT_BUTTON)).click()





