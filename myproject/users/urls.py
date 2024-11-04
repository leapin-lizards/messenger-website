from django.urls import path
from . import views
app_name='users'
urlpatterns = [
    path('',views.users_list,name="list"),
    path('<int:userid>',views.user_page,name="page"),
    path('register',views.user_register,name="register"),
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout")
]