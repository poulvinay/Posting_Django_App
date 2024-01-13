from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name= 'home' ),
    path('home/', views.home, name= 'home' ),
    path('account/signin', views.signin, name = 'signin'),
    path('account/', include('django.contrib.auth.urls')),
    path('create-post', views.create_post, name='create_post'),
    path('<str:username>', views.user_profile, name='user_profile'),
    
]