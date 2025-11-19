import time
from base.base_test import BaseTest


class TestShopp(BaseTest):

    def test_open(self):
        self.login_page.open()
        self.login_page.login(
            login=self.credentials.LOGIN,
            password=self.credentials.PASSWORD
        )

        self.products_page.open()
        self.products_page.is_opened()
        self.products_page.add_product_to_cart()
        #self.products_page.cart_badge()
        self.products_page.cart()

        time.sleep(3)

        # self.your_cart_page.open()
        # self.your_cart_page.is_opened()
        # self.your_cart_page.chechout()
        #
        # time.sleep(3)
        #
        # self.chechout_your_information_page.open()
        # self.chechout_your_information_page.is_opened()
        # self.chechout_your_information_page.data_entry(
        #     name=self.credentials.NAME,
        #     surname=self.credentials.SURNAME,
        #     index=self.credentials.INDEX
        # )
        # time.sleep(3)




