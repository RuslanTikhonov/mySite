from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='home'),
    path('news/add', views.CreateNewsView.as_view(), name='news-add'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<str:username>', views.UserAllNewsView.as_view(), name='user-news'),
    path('news/<int:pk>/update', views.UpdateNewsView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='news-delete'),
    path('contacti', views.contacti, name='contacti'),

]