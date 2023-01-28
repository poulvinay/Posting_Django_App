from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home' ),
    path('home/', views.home, name= 'home' ),
    path('signin', views.signin, name = 'signin'),
    path('create-post', views.create_post, name='create_post'),
    path('<str:username>', views.user_profile, name='user_profile'),
]