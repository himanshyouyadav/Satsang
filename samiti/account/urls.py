from django.contrib import admin
from django.urls import include, path

from account.views import change_password, dashboard, error_page, forget_password, home, homepage, login, register, success, token_send, verify,logout

urlpatterns = [
    path('',homepage),
    path('homepage',homepage),
    path('dashboard',dashboard),
    path('login',login,name="login_attempt"),
    path('register',register,name="register_attempt"),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('logout',logout,name='logout'),
    path('forget_password',forget_password,name = "forget_password"),
    path('resetpassword/<auth_token>',change_password,name = "change_password"),

]