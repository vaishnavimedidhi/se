from django.urls import reverse,resolve
from django.test import TestCase


class TestUrls(TestCase):

	#Testing Profiles
	def test_searchAuthors_url(self):
		path = reverse('searchAuthors')
		assert resolve(path).view_name=='searchAuthors'

	def test_singleauthor_url(self):
		path = reverse('SingleAuthor',kwargs = {'authorName':'Andrew Ng'})
		assert resolve(path).view_name=='SingleAuthor'

	def test_singlepublication_url(self):
		path = reverse('SinglePublication',kwargs={'authorName':'Andrew Ng','pubind':0})
		assert resolve(path).view_name=='SinglePublication'