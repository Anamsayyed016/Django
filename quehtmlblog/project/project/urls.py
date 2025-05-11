"""
URL configuration for project project.

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
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),

    path('home/',views.home,name='home'),
    path('home1/<int:pk>',views.home1,name='home1'),

    path('about/',views.about,name='about'),
    path('about1/<int:pk>',views.about1,name='about1'),

    path('recipes/',views.recipes,name='recipes'),
    path('recipes1/<int:pk>',views.recipes1,name='recipes1'),

    path('video/',views.video,name='video'),
    path('video1/<int:pk>',views.video1,name='video1'),

    path('register/',views.register,name='register'),
    path('registerdetail/',views.registerdetail,name='registerdetail'),

    path('login/',views.login,name='login'),
    path('logiinfo/',views.logiinfo,name='logiinfo')






]
