from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from profiles.views import searchAuthors


class ProfilesTest(TestCase):

	def test_profiles_searchAuthors_view(self):
		w = self.create_searchAuthors()
		url  = reverse("profiles.views.searchAuthors")
		resp = self.client.get(url)


		self.asserEqual(resp.status_code, 200)
		self.assertIn(w.title,resp.content)
