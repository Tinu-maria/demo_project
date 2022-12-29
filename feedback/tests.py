from django.test import TestCase
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from feedback.models import Feedback
from datetime import date
from unittest import mock
from feedback.functions import mock_date
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Mock test

def mock_today():
    return date(year=2022, month=12, day=20)
 
class UnitTestMock(TestCase):
    @mock.patch("feedback.functions.get_today", mock_today)
    def test_func_date(self):
        self.assertEqual(mock_date().strftime("%Y-%m-%d"), "2022-12-20")

# Liveserver testcase

class ExampleTestCase(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")
        super(ExampleTestCase, self).setUp()

    def test_example(self):
        self.driver.get(("%s%s" % (self.live_server_url, "/admin/")))
        assert "Log in | Django site admin" in self.driver.title

    def tearDown(self):
        self.driver.quit()
        super(ExampleTestCase, self).tearDown()

class SeleniumTestCase(LiveServerTestCase):
    def setUp(self):
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/login/')

        username = selenium.find_element(By.NAME,'username')
        password = selenium.find_element(By.NAME,'password')
        submit = selenium.find_element(By.ID,'submit')

        username.send_keys('test')
        password.send_keys('test')
        submit.send_keys(Keys.RETURN)
        
        assert "test" in selenium.page_source

class LoginTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome("./chromedriver")
        super(LoginTestCase, self).setUp()

    def test_register(self):
        selenium = self.selenium
        selenium.get(("%s%s" % (self.live_server_url, "/login/")))
        username = selenium.find_element(By.ID,'id_username')
        password = selenium.find_element(By.ID,'id_password')
        submit = selenium.find_element(By.ID,'submit')

        username.send_keys('test')
        password.send_keys('test')
        submit.send_keys(Keys.ENTER)

        # wait = WebDriverWait(selenium, 10)
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".list-recent-events li")))

        assert "login" in selenium.page_source    

    def tearDown(self):
        self.selenium.quit()
        super(LoginTestCase, self).tearDown()   

class RegisterTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome("./chromedriver")
        self.user1 = User.objects.create(
            username="testing",
            first_name="testing",
            last_name="testing",
            email="testing@gmail.com",
            password="testing",
        )
        super(RegisterTestCase, self).setUp()

    def test_register(self):
        selenium = self.selenium
        selenium.get(("%s%s" % (self.live_server_url, "/register/")))
        username = selenium.find_element(By.ID,'id_username')

        username.send_keys('testing')
        username.send_keys(Keys.ENTER)   

        # wait = WebDriverWait(selenium, 10)
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".list-recent-events li")))

        assert "register" in selenium.page_source  

    def tearDown(self):
        self.selenium.quit()
        super(RegisterTestCase, self).tearDown()

# Unittest

class TestModel(TestCase):
    def test_model(self):
        feedback = Feedback.objects.create(email='tinu@gmail.com',message='good feedback')
        self.assertEqual(str(feedback), 'tinu@gmail.com')

class UserTesting(TestCase):
    def setUp(self):
        User.objects.create(username="test1", password="test")
        User.objects.create(username="test2", password="test")
    
    def test_user(self):
        user1 = User.objects.get(username="test1")
        user2 = User.objects.get(username="test2")
        self.assertEqual(str(user1), "test1")
        self.assertEqual(str(user2), "test2")
