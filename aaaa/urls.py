from . import views
from django.urls import path

app_name = "aaaa"
urlpatterns = [
    path('index', views.index, name='index'),
    # 正しいパターンに修正
    path('index2', views.index2, name='index2'),
    path('ques', views.ques, name='ques'),
    path('<int:article_id>/update', views.update, name='update'),
    path('hello', views.hello, name='hello'),
    path('redirect', views.redirect_test, name='redirect_test'),
    path('<int:article_id>/', views.article_detail, name='detail'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/delete', views.delete, name='delete'),
    #path('<int:article_id>/update', views.update, name='update'),
]