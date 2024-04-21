"""
URL configuration for labs6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('agents/', views.agent_list, name='agent_list'),
    path('agents/<int:id>/', views.agent_detail, name='agent_detail'),
    path('agents/create/', views.agent_create, name='agent_create'),
    path('agents/<int:id>/update/', views.agent_update, name='agent_update'),
    path('agents/<int:id>/delete/', views.agent_delete, name='agent_delete'),

    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:id>/', views.property_detail, name='property_detail'),
    path('properties/create/', views.property_create, name='property_create'),
    path('properties/<int:id>/update/', views.property_update, name='property_update'),
    path('properties/<int:id>/delete/', views.property_delete, name='property_delete'),

    path('clients/', views.client_list, name='client_list'),
    path('clients/<int:id>/', views.client_detail, name='client_detail'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/<int:id>/update/', views.client_update, name='client_update'),
    path('clients/<int:id>/delete/', views.client_delete, name='client_delete'),

    path('requests/', views.request_list, name='request_list'),
    path('requests/<int:id>/', views.request_detail, name='request_detail'),
    path('requests/create/', views.request_create, name='request_create'),
    path('requests/<int:id>/update/', views.request_update, name='request_update'),
    path('requests/<int:id>/delete/', views.request_delete, name='request_delete'),

    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('users/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),
]

