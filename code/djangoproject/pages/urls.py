
from django.urls import path
from pages.views import home, about
urlpatterns = [
  	path('', home, name='home'),
    path('about-us/', about, name='about'),
]