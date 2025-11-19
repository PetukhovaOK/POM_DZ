from base.base_page import BasePage
from data.urls import Urls
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage(BasePage):

    _PAGE_URL = Urls.PRODUCTS_PAGE

    _ADD_PRODUCT_TO_CART = "//button[@id='add-to-cart-sauce-labs-backpack']"
    _CART_BADGE = "//span[@data-test='shopping-cart-badge']"
    _CART = "//a[@data-test='shopping-cart-link']"

    # добавление товара в корзину
    def add_product_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self._ADD_PRODUCT_TO_CART)).click()

    # проверка индикатора корзины
    def cart_badge(self, _CART_BADGE=None):
        self.wait.until((EC.presence_of_element_located(self._CART_BADGE)))
        return int(_CART_BADGE.text)

    # переходим в корзину
    def cart(self):
        self.wait.until(EC.element_to_be_clickable(self._CART)).click()
