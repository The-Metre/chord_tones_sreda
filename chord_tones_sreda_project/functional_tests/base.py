import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class FunctionalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')

        self.browser = webdriver.Chrome(options=self.options)

    def tearDown(self) -> None:
        self.browser.quit()


    def test_starting_page(self):

        self.browser.get('http://localhost:8000')

        body = self.browser.find_element(By.TAG_NAME, 'body')
        page_text = body.text

        self.assertAlmostEqual('Test view',page_text)


if __name__ == '__main__':
    unittest.main(warnings='ignore')