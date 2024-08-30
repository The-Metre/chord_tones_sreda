from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


MAX_WAIT = 5

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')

        self.browser = webdriver.Chrome(options=self.options)

    def tearDown(self) -> None:
        self.browser.quit()

    def wait(fn):
        def modified_fn(*args, **kwargs):
            start_time = time.time()
            while True:
                try:
                    return fn(*args, **kwargs)
                except (AssertionError, WebDriverException) as e:
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.5)
        return modified_fn

    @wait
    def wait_for(self, fn):
        return fn()
    
if __name__ == '__main__':
    StaticLiveServerTestCase.main(warnings='ignore')