from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('stores/', views.getStores),
    path('stores/create/', views.createStore),
    path('stores/<str:pk>/update/', views.updateStore),
    path('stores/<str:pk>/delete/', views.deleteStore),
    path('store/<str:pk>/', views.getStore),
]