"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task2.views import index, Index2, page
from task3.views import home_page, shop, shopping_cart
from task4.views import home_page1, shop1, shopping_cart1
from task5.views import page1, sign_up_by_html, sign_up_by_django
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page),
    path('index/', index),
    path('index1/', Index2.as_view()),
    path('index2/', TemplateView.as_view(template_name='second_task/class_templates.html')),

    path('home_page/', home_page),
    path('shop/', shop),
    path('shopping_cart/', shopping_cart),

    path('home_page1/', home_page1),
    path('shop1/', shop1),
    path('shopping_cart1/', shopping_cart1),

    path('home_page2/', page1),
    path('html_sign_up/', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django),
]
