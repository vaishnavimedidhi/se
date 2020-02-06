from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from authentication.views import *
from mixer.backend.django import mixer
from django.test import TestCase


class Testview(TestCase):

	def setUp(self):
		self.credentials = {
			'username':'testuser',
			'password':'secret@1'
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


		response = signin(request)
		assert response.status_code==200

	def test_signup(self):
		path = reverse('signup')
		request = RequestFactory().get(path)

		response = signup(path)
		assert response.status_code==200


	def test_dashboard(self):
		path = reverse('dashboard')
		request = RequestFactory().get(path)

		response = dashboard(request)
		assert response.status_code==200

	def test_edit(self):
		path = reverse('edit')
		request = RequestFactory().get(path)

		response = edit(response)
		assert response.status_code==200

	def test_status(self):
		path = reverse('status')
		request = RequestFactory().get(path)

		response = status(response)
		assert response.status_code==200

	def test_ratings(self):
		path = reverse('ratings')
		request = RequestFactory().get(path)

		response = ratings(response)
		assert response.status_code==200