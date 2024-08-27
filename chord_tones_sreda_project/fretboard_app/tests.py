from functional_tests.base import FunctionalTest
from selenium.webdriver.common.by import By
# Create your tests here.


class FretboardPageTest(FunctionalTest):
    """
    basic test to ensure that browser opens homepage of a project
    """
    def test_url_can_redirect_to_fretboard_page(self):
        pass
        """self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertEquals(body.text, 'Fretboard')"""

