from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('part_two', views.advanced, name="index"),
	path('initialize', views.make_data, name="make_data"),
]
