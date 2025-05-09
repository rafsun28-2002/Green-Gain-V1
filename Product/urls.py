"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('products/', product, name='product'),
    path('products/<str:category>/', category_detail, name='category_detail'),
    path('products/<str:category>', vegetable, name='vegetable'),
    path('fruits/', fruit, name='fruit'),
    path('meat/', meat, name='meat'),
    path('fish/', river_fish, name='river-fish'),
    path('spices/', spice, name='spice'),
    path('create-plan/', create_plan, name='create_plan'),
    path('select-product/', select_product, name='select_product'),
    path('checkout/', checkout, name='checkout'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('checkout/', checkout, name='checkout'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])