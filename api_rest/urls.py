from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_characters, name='get_all_characters'),
    path('character/<str:nick>', views.get_by_nick),
]

