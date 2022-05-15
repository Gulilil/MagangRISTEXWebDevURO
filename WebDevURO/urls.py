"""WebDevURO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from homepage.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('pilah_sampah/', tema1, name='tema1'),
    path('berwawasan_lingkungan/', tema7, name='tema7'),
    path('3R/', tema8, name='tema8'),
    path('kurangi_penggunaan_plastik/', tema12, name='tema12'),
    path('admin/', admin.site.urls),
]
