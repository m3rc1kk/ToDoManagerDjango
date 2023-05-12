from django.urls import path
from .views import *

urlpatterns = [
    path("info/", UserInfo, name="user-info"),
    path("register/", RegisterUser, name= 'user-register'),
    path("login/", LoginUser.as_view(), name= 'user-login'),
    path("logout/", LogoutUser.as_view(), name= 'user-logout'),
    path("update/", UpdateInfoUser, name= 'user-update'),
]
