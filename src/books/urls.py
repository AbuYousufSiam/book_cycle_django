from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#.......this is to call the booklistview.................................
from .views import BooksListView

urlpatterns = [
    #........rander the login and sign up option............
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    #......this path is to show the list of books............
    path('index/', BooksListView.as_view(), name='index'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]