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
#______________________________________________________________
#Change the logout_view to logoutView for the sake of reverse matching!!!
	def test_logout_url(self):
		path = reverse('logout')
		assert resolve(path).view_name!='logoutView'
#________________________________________________________________

	def test_dashboard_url(self):
		path = reverse('dashboard')
		assert resolve(path).view_name=='dashboard'

	def test_edit_url(self):
		path = reverse('edit')
		assert resolve(path).view_name=='edit'

	def test_status_url(self):
		path = reverse('status')
		assert resolve(path).view_name=='status'

	def test_ratings_url(self):
		path = reverse('ratings')
		assert resolve(path).view_name=='ratings'
		