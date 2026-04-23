from unittest import TestCase
from src.service.web_driver import host_app, shutdown_app
from selenium import webdriver

class WebDriverTest(TestCase):
    @classmethod
    def setUpClass(self):
        host_app(3000)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=options)
        self.base_url = "localhost:3000"
    @classmethod
    def tearDownClass(self):
        shutdown_app()
        self.browser.quit()
    
    def test_app_is_healthy(self):
        self.browser.get(self.base_url + "/")
        text = self.browser.find_element("tag name", "body").text
        self.assertEqual(text, "The server is healthy")
