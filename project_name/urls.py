"""
URL configuration for project_name project.

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
from noteapp.views import index,delete_note,edit_note

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path( 'delete/<int:id>',delete_note,name="delete_note"),
    path( 'edit/<int:id>',edit_note,name="edit_note"),
]
