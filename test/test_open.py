import time
from base.base_test import BaseTest


class TestShopp(BaseTest):

# вводим логин, пароль, кликаем на кнопку авторизации
    def test_open(self):
        self.login_page.open()
        self.login_page.login(
            login=self.credentials.LOGIN,
            password=self.credentials.PASSWORD
        )

    # открытие страницы выбора товара
        self.products_page.open()
        time.sleep(3)
    # проверка, что открыта нужная страница
        self.products_page.is_opened()
        time.sleep(3)
    # добавление товара в корзину
        self.products_page.add_product_to_cart()
        time.sleep(3)
    # проверяем, что товары в корзине
        #self.products_page.cart_badge()
    # переход в корзину кликом на икноку корзины
        self.products_page.cart()
        time.sleep(3)

    # открытие страницы корзины
        self.your_cart_page.open()
        time.sleep(3)
    # проверка, что открыта нужная страница
        self.your_cart_page.is_opened()
        time.sleep(3)
    # на странице корзины нажимаем кнопку Checkout
        self.your_cart_page.chechout_button()

        time.sleep(3)

    # открытие страницы ввода данных покупателя
        self.chechout_your_information_page.open()
        time.sleep(3)
    # проверка, что открыта нужная страница
        self.chechout_your_information_page.is_opened()
        time.sleep(3)
    # ввод имени, фамилии, почтового индекса и нажатие кнопки Continue
        self.chechout_your_information_page.data_entry(
            name=self.credentials.NAME,
            surname=self.credentials.SURNAME,
            index=self.credentials.INDEX
        )
        time.sleep(3)

    # открытие страницы подтверждения оформления заказа
        self.chechout_overview_page.open()
    # проверка, что открыта нужная страница
        self.chechout_overview_page.is_opened()
    # нажатие кнопки Finish:
        self.chechout_overview_page.finish_button()

    # открытие страницы завершения оформления заказа
        self.chechout_complete_page.open()
    # проверка, что открыта нужная страница
        self.chechout_complete_page.is_opened()





