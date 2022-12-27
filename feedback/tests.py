# from django.test import TestCase
# from django.contrib.auth.models import User
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from feedback.models import Feedback, Profile
# from datetime import date
# from unittest import mock
# from feedback.functions import mock_date
# from feedback.views import LoginView

# # Mock test

# def mock_today():
#     return date(year=2022, month=12, day=20)
 
# class UnitTestMock(TestCase):
#     @mock.patch("feedback.functions.get_today", mock_today)
#     def test_func_date(self):
#         self.assertEqual(mock_date().strftime("%Y-%m-%d"), "2022-12-20")

# # Unittest

# class TestModel(TestCase):
#     def test_model(self):
#         feedback = Feedback.objects.create(email='tinu@gmail.com',message='good feedback')
#         self.assertEqual(str(feedback), 'tinu@gmail.com')

# class UserTesting(TestCase):
#     def setUp(self):
#         User.objects.create(username="test1", password="test")
#         User.objects.create(username="test2", password="test")

#     # def test_case(self):
#     #     with mock.patch("feedback.views.LoginView") as fetch_login:
#     #         fetch = LoginView(username='tinu', password='tinu')
#     #         fetch_login.return_value = fetch
#     #         self.assertEqual(fetch)
    
#     def test_user(self):
#         user1 = User.objects.get(username="test1")
#         user2 = User.objects.get(username="test2")
#         self.assertEqual(str(user1), "test1")
#         self.assertEqual(str(user2), "test2")

# # Liveserver testcase

# class ExampleTestCase(LiveServerTestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome("./chromedriver")
#         super(ExampleTestCase, self).setUp()

#     def tearDown(self):
#         self.driver.quit()
#         super(ExampleTestCase, self).tearDown()

#     def test_example(self):
#         self.driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in self.driver.title

# class SeleniumTestCase(LiveServerTestCase):
#     def setUp(self):
#         self.selenium = webdriver.Chrome("./chromedriver")
#         super(SeleniumTestCase, self).setUp()

#     def tearDown(self):
#         self.selenium.quit()
#         super(SeleniumTestCase, self).tearDown()

#     def test_register(self):
#         selenium = self.selenium
#         selenium.get(("%s%s" % (self.live_server_url, "/login/")))
#         username = selenium.find_element(By.ID,'id_username')
#         password = selenium.find_element(By.ID,'id_password')
#         submit = selenium.find_element(By.ID,'submit')

#         username.send_keys('test')
#         password.send_keys('test')
#         submit.send_keys(Keys.ENTER)

#         assert "Django App" in self.selenium.title

# class RegisterTestCase(LiveServerTestCase):
#     def setUp(self):
#         self.selenium = webdriver.Chrome("./chromedriver")
#         self.user1 = User.objects.create(
#             username="testing",
#             first_name="testing",
#             last_name="testing",
#             email="testing@gmail.com",
#             password="testing",
#         )
#         super(RegisterTestCase, self).setUp()

#     def tearDown(self):
#         self.selenium.quit()
#         super(RegisterTestCase, self).tearDown()

#     def test_register(self):
#         selenium = self.selenium
#         selenium.get(("%s%s" % (self.live_server_url, "/register/")))
#         username = selenium.find_element(By.ID,'id_username')

#         username.send_keys('testing')
#         username.send_keys(Keys.ENTER)   

