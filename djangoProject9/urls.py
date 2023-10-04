"""
URL configuration for djangoProject9 project.

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

from django.urls import path
from architecture import views

urlpatterns = [
    path('users/', views.UserCreateView.as_view(), name='user-create'),
    path('products/', views.ProductCreateView.as_view(), name='product-create'),
    path('product-access/', views.ProductAccessCreateView.as_view(), name='product-access-create'),
    path('lessons/', views.LessonCreateView.as_view(), name='lesson-create'),
    path('viewing-history/', views.ViewingHistoryCreateView.as_view(), name='viewing-history-create'),
    path('api/<int:user_id>/', views.HistoryAPIView.as_view(), name='HistoryAPIView'),
    path('api/users/<int:user_id>/<int:product_id>/', views.ProductLessonAPIView.as_view(), name='product-lessons'),
    path('api/product_stats/', views.ProductStatsAPIView.as_view(), name='ProductStatsAPIView'),
]