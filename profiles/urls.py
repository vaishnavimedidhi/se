from django.urls import path
from .views import searchAuthors,SingleAuthor,SinglePublication

urlpatterns = [

	#path('',searchAuthors,name='call_searchAuthors'),
	path('searchauthor/',searchAuthors,name='searchAuthors'),
	path("profile/<str:authorName>/",SingleAuthor,name='SingleAuthor'),
	path("publication/<str:authorName>/<int:pubind>",SinglePublication,name='SinglePublication'),

]