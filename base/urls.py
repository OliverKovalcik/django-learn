from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.articles, name="articles"),
    path('create-article/', views.createArticle, name='create-article')
]
