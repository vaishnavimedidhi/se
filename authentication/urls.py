from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index , name='index'),
    path('signin/', views.signin , name='signin'),
    path('signup/', views.signup , name='signup') ,
    path('logout/',views.logoutView , name = 'logout'),
    path('dashboard/' , views.dashboard , name ='dashboard'),
    path('dashboard/edit/' , views.edit , name ='edit'),
    path('dashboard/status/',views.status , name ='status'),
    path('dashboard/ratings/' , views.ratings , name= 'ratings')

]

