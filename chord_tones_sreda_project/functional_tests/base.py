from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')

        self.browser = webdriver.Chrome(options=self.options)

    def tearDown(self) -> None:
        self.browser.quit()


if __name__ == '__main__':
    StaticLiveServerTestCase.main(warnings='ignore')