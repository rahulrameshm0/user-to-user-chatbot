from django.urls import path
from . import views
urlpatterns = [
    path('', views.sign_in, name='login'),
    path('home/', views.home, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.sign_out, name='logout'),
    path('chat/<str:username>/', views.chat_user, name='chat_user'),
    # path('user_lists', views.user_lists, name='user_lists'),
]
