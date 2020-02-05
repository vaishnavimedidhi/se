from django.urls import resolve,reverse


class Testurls:

	def test_open_url(self):
		path = reverse('index')
		assert resolve(path).view_name=='index'

	def test_signin_url(self):
		path = reverse('signin')
		assert resolve(path).view_name=='signin'

	def test_signup_url(self):
		path = reverse('signup')
		assert resolve(path).view_name=='signup'

	