from functional_tests.base import FunctionalTest
from selenium.webdriver.common.by import By
# Create your tests here.

class HomePageTest(FunctionalTest):
    """
    basic test to ensure that browser opens homepage of a project
    """
    def test_root_url_resolve_to_home_page(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertEquals(body.text, 'Test view')


    def test_home_page_uses_base_template(self):
        
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html') 

