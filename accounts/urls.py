from django.urls import path
from . import views

from django.urls import path


app_name = "accounts"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout", views.LoginView.as_view(), name="logout"),  # 追加
    path("inf", views.inf.as_view(), name="inf"), 

    
    #path('<int:article_id>/update', views.update, name="update"),

    
]