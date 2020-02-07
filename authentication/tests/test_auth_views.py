from django.test import RequestFactory,Client
from django.urls import reverse
from django.contrib.auth.models import User
from authentication.views import *
from mixer.backend.django import mixer
from django.test import TestCase
from authentication.models import *


class Testview(TestCase):

	def setUp(self):
		self.credentials = {
			'username':'Bavish',
			'password':'bavishprasath'
		}
		User.objects.create_user(**self.credentials)
	def test_index(self):
		path = reverse('index')
		request = RequestFactory().get(path)

		response = index(request)
		assert response.status_code==200

#testing signin view

	def test_signin(self):
	
		path = reverse('signin')
		request = RequestFactory().get(path)
		print(request)

		c = Client()
		response = c.post('/signin/',{'username':'Bavish','password':'bavishprasath'},follow=True)
		assert response.status_code==200

	def test_signup(self):
		path = reverse('signup')
		request = RequestFactory().get(path)

		c = Client()
		response = c.post('/signup/',{'name':'tester','email':'tester@gmail.com','gender':1,'acheivement':'None','stream':'None','contact_number':12346789,'url':'Nothing','password':'secretismine','accounttype':'professor'})
		print(response)
		response = c.post('/signin/',{'username':'tester','password':'secretismine'},follow=True)
		assert response.status_code==200
	def test_signup_student(self):
		c = Client()
		response = c.post('/signup/',{'name':'testerstudent','email':'tester@gmail.com','gender':1,'acheivement':'None','stream':'None','contact_number':12346789,'url':'Nothing','password':'secretismine','accounttype':'Student'})
		print(response)
		response = c.post('/signin/',{'username':'tester','password':'secretismine'},follow=True)
		assert response.status_code==200

	def test_warn_signin(self):
		c = Client()
		response = c.post('/signin/',{'username':'tester','password':'secretisnotmine'},follow=True)
		print(response.context['msg'])
		assert response.context['msg']=='wrong password/username'

	def test_notpost_signin(self):
		c = Client()
		response = c.get('/signin/',{'username':'tester','password':'secretisnotmine'},follow=True)
		print(response.context['msg'])
		assert response.context['msg']=='.'

	def test_dashboard_professor(self):
		c = Client()
		response = c.post('/signup/',{'name':'tester','email':'tester@gmail.com','gender':1,'acheivement':'None','stream':'None','contact_number':12346789,'url':'Nothing','password':'secretismine','accounttype':'professor'})
		response = c.post('/signin/',{'username':'tester','password':'secretismine'})
		response = c.get('/dashboard/',{'username':'tester'},follow=True)
		assert response.context['accounttype']=='professor'

	def test_dashboard_student(self):
		c = Client()
		response = c.post('/signup/',{'name':'tester','email':'tester@gmail.com','gender':1,'acheivement':'None','stream':'None','contact_number':12346789,'url':'Nothing','password':'secretismine','accounttype':'student'})
		response = c.post('/signin/',{'username':'tester','password':'secretismine'})
		response = c.get('/dashboard/',{'username':'tester'},follow=True)
		assert response.context['accounttype']=='student'

	def test_edit(self):
		c = Client()
		response = c.post('/signup/',{'name':'tester','email':'tester@gmail.com','gender':1,'acheivement':'None','stream':'None','contact_number':12346789,'url':'Nothing','password':'secretismine','accounttype':'professor'})
		response = c.post('/signin/',{'username':'tester','password':'secretismine'})
		response = c.post('/dashboard/edit/',{'email':'tester@gmail.com','acheivement':'acheivement','stream':'stream','contact_number':987654321})
		assert response.url=='/dashboard/'

	def test_edit_student(self):
		c = Client()
		response = c.post('/signup/',{'name':'tester','email':'tester@gmail.com','gender':1,'acheivement':'None','stream':'None','contact_number':12346789,'url':'Nothing','password':'secretismine','accounttype':'student'})
		response = c.post('/signin/',{'username':'tester','password':'secretismine'})
		response = c.post('/dashboard/edit/',{'email':'tester@gmail.com','acheivement':'acheivement','stream':'stream','contact_number':987654321})
		assert response.url=='/dashboard/'

	def test_logOut(self):
		c = Client()
		response = c.post('/signup/',{'name':'tester','email':'tester@gmail.com','gender':1,'acheivement':'None','stream':'None','contact_number':12346789,'url':'Nothing','password':'secretismine','accounttype':'professor'})
		response = c.post('/signin/',{'username':'tester','password':'secretismine'})
		response = c.get('/logout/')
		print(response)
		assert response.status_code==302




	# def test_status(self):
	# 	path = reverse('status')
	# 	request = RequestFactory().get(path)

	# 	response = status(response)
	# 	assert response.status_code==200

	# def test_ratings(self):
	# 	path = reverse('ratings')
	# 	request = RequestFactory().get(path)

	# 	response = ratings(response)
	# 	assert response.status_code==200