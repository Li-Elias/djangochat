from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('home_submit', views.home_submit, name='home_submit'),
    path('message', views.message, name='message'),
    path('get_messages/<str:room>/', views.get_messages, name='get_messages')
]
