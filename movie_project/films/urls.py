from django.urls import path
from . import views

# Указываем пути к страницам приложения
urlpatterns = [
	path('', views.home, name='films_home'),
	path('create', views.create_film, name='add_film'),
]