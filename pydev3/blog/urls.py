from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('hello/', views.Hello.as_view(), name='hello'),
    path('create/', views.BlogCreate.as_view(), name='blog_create'),
    path('list/', views.BlogList.as_view(), name='blog_list'),
]