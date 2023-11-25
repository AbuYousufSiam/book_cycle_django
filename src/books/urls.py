from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# .......this is to call the booklistview.................................
from .views import BooksListView
from .views import update

urlpatterns = [
    path("update_server/", views.update, name="update"),
    path("touch_wsgi/", views.touch_wsgi, name="touch_wsgi"),
    # ........rander the login and sign up option............
    path("", views.index, name="home"),
    path("login/", views.user_login, name="login"),
    # ......this path is to show the list of books............
    path("index/", BooksListView.as_view(), name="index"),
    path("signup/", views.signup, name="signup"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("add_book/", views.add_book, name="add_book"),
    path("update_book/<int:book_id>/", views.update_book, name="update_book"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
]
