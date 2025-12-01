from base.base_page import BasePage
from data.urls import Urls
from selenium.webdriver.support import expected_conditions as EC

class ChechoutOverviewPage(BasePage):

    _PAGE_URL = Urls.CHECHOUT_OVERVIEW_PAGE

    _FINISH_BUTTON = "//button[@id='finish']"

# нажимаем на кнопку Finish:
    def finish_button(self):
        self.wait.until(EC.element_to_be_clickable(self._FINISH_BUTTON)).click()
