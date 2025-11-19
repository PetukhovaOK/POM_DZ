from base.base_page import BasePage
from data.urls import Urls
from selenium.webdriver.support import expected_conditions as EC

class ChechoutYourInformationPage(BasePage):

    _PAGE_URL = Urls.CHECHOUT_YOUR_INFORMATION_PAGE

    _FIRST_NAME_FIELD = "//input[@id='first-name']"
    _LAST_NAME_FIELD = "//input[@id='last-name']"
    _POSTAL_CODE_FIELD = "//input[@id='postal-code']"
    _CONTINUE_BUTTON = "//input[@id='continue']"

# вводим имя, фамилию, почтовый индекс и нажимаем кнопку Continue
    def data_entry(self, name, surname, index):
        self.wait.until(EC.element_to_be_clickable(self._FIRST_NAME_FIELD)).send_keys(name)
        self.wait.until(EC.element_to_be_clickable(self._LAST_NAME_FIELD)).send_keys(surname)
        self.wait.until(EC.element_to_be_clickable(self._POSTAL_CODE_FIELD)).send_keys(index)
        self.wait.until(EC.element_to_be_clickable(self._CONTINUE_BUTTON)).click()



