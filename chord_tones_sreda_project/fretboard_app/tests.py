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


    def test_fretboard_div_shown_on_the_page(self):
        self.browser.get('http://127.0.0.1:8000/fretboard')
        self.wait_for(lambda: self.assertEquals(
            'Test fretboard div',
            self.browser.find_element(By.CLASS_NAME, 'fretboard').text
        ))