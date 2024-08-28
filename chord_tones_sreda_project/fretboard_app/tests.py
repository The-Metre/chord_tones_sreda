from functional_tests.base import FunctionalTest
from selenium.webdriver.common.by import By
# Create your tests here.


class FretboardPageTest(FunctionalTest):
    """
    basic test to ensure that page uses correct template
    """
    def test_url_can_redirect_to_fretboard_page(self):
        
        response = self.client.get('/fretboard')
        self.assertTemplateUsed(response, 'fretboard.html')

