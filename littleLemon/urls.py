"""
URL configuration for littleLemon project.

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
from django.urls import path, include 

from lit_lemon.views import home, about, menu, book ,display_menu_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('home/', home), 
    path('menu/', menu),
    path('book/', book),
    path('menu_item/<int:pk>/', display_menu_item, name="menu_item"),
]
