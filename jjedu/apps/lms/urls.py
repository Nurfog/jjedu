from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from . import settings, views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),


