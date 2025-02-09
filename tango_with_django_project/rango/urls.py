
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('category/<slug:category_name_slug>/add_page/', views.add_page,
name='add_page'),
path('category/<slug:category_name_slug>/', views.show_category,
name='show_category'),
path('add_category/', views.add_category, name='add_category'),
path('register/', views.register, name='register'), # New mapping!
path('restricted/', views.restricted, name='restricted'),
]