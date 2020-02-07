from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import RequestFactory,Client
from django.urls import reverse
from django.contrib.auth.models import User
from authentication.views import *
from mixer.backend.django import mixer
from django.test import TestCase
from authentication.models import *
import time

class AuthenticationTestCase(LiveServerTestCase):

	def setUp(self):
		self.selenium = webdriver.Chrome(executable_path = r"C:\\Users\\ayyap\\OneDrive\\Desktop\\scraping\\chromedriver_win32\\chromedriver.exe")
		super(AuthenticationTestCase,self).setUp()

	def tearDown(self):
		self.selenium.quit()
		super(AuthenticationTestCase,self).tearDown()

	def test_register(self):
		selenium = self.selenium

		selenium.get('http://127.0.0.1:8000/signup/')

		

		email = selenium.find_element_by_id('email')
		email.send_keys('mytester@gmail.com')

		name = selenium.find_element_by_id('name')
		name.send_keys('mytesterone')

		password = selenium.find_element_by_id('password')
		password.send_keys('firstone')

		phone = selenium.find_element_by_id('phonenumber')
		phone.send_keys('123456789')

		achieve = selenium.find_element_by_id('acheivements')
		achieve.send_keys('first of my kind')

		stream = selenium.find_element_by_id('stream')
		stream.send_keys('cse')

		url = selenium.find_element_by_id('reflink')
		url.send_keys('http://hem1999/github.io')


		gender = selenium.find_element_by_id('female')
		time.sleep(5)
		selenium.execute_script("arguments[0].click();", gender)
		


		register = selenium.find_element_by_id('registerbutton')
		time.sleep(5)
		register.click()


		c = Client()
		response = c.post('/signin/',{'username':'mytesterone','password':'firstone'})
		assert response.status_code==200


	def test_register_professor(self):
		selenium = self.selenium

		selenium.get('http://127.0.0.1:8000/signup/')
		time.sleep(2)
		prof = selenium.find_element_by_id('radioTwo')
		time.sleep(5)
		selenium.execute_script("arguments[0].click();", prof)

		email = selenium.find_element_by_id('email')
		email.send_keys('mytesterf@gmail.com')

		name = selenium.find_element_by_id('name')
		name.send_keys('mytesteronef')

		password = selenium.find_element_by_id('password')
		password.send_keys('firstonef')

		phone = selenium.find_element_by_id('phonenumber')
		phone.send_keys('123456789')

		achieve = selenium.find_element_by_id('acheivements')
		achieve.send_keys('first of my kind')

		stream = selenium.find_element_by_id('stream')
		stream.send_keys('cse')

		url = selenium.find_element_by_id('reflink')
		url.send_keys('http://hem1999/github.io')
		time.sleep(2)


		time.sleep(5)

		gender = selenium.find_element_by_id('female')
		selenium.execute_script("arguments[0].click()",gender)
		time.sleep(5)


		register = selenium.find_element_by_id('registerbutton')
		register.click()


		c = Client()
		response = c.post('/signin/',{'username':'mytesteronef','password':'firstonef'})
		assert response.status_code==200

	def test_signin_student(self):

		selenium = self.selenium
		selenium.get('http://127.0.0.1:8000/signin/')

		username = selenium.find_element_by_id('login__username')
		username.send_keys('Bavish')

		password = selenium.find_element_by_id('login__password')
		password.send_keys('bavishprasath')

		submitbtn = selenium.find_element_by_id('submit_button')
		time.sleep(3)
		submitbtn.click()


	def test_search_link(self):
		selenium = self.selenium
		selenium.get('http://127.0.0.1:8000')

		link = selenium.find_element_by_id('searchauthorlink')
		time.sleep(3)
		link.click()

	def test_seach_bar(self):

		selenium = self.selenium
		selenium.get('http://127.0.0.1:8000/searchauthor/searchauthor/')

		box = selenium.find_element_by_id('searchhere')
		box.send_keys('Andrew')
		time.sleep(3)
		btn = selenium.find_element_by_id('submitbutton')
		btn.click()

	def testing_checkprofile_link(self):
		selenium = self.selenium
		selenium.get('http://127.0.0.1:8000/searchauthor/searchauthor/')

		link = selenium.find_element_by_id('checkoutprofilelink')
		time.sleep(2)
		link.click()

	def testing_eachpublication_link(self):
		selenium = self.selenium
		selenium.get('http://127.0.0.1:8000/searchauthor/profile/Hector%20Perla%20Jr./')

		link = selenium.find_element_by_id('publication 0')
		time.sleep(2)
		link.click()

