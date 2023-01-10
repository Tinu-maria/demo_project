from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Create your tests here.

class SeleniumTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()

    def test_register(self):
        self.selenium.get('http://127.0.0.1:8000/login/')
        self.selenium.find_element_by_name('username').send_keys('test')
        self.selenium.find_element_by_name('password').send_keys('test')
        # first_name = selenium.find_element_by_name('first_name')
        # last_name = selenium.find_element_by_name('last_name')
        # email = selenium.find_element_by_name('email')

        self.selenium.find_element_by_id('submit').click()
        self.assertIn("http://localhost:8000/", self.driver.current_url)

    def tearDown(self):
        self.selenium.quit()
