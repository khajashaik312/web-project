"""
URL configuration for ideadev project.

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
# urls.py
'''from django.contrib import admin
from django.urls import path
from myapp.views import delete_contact_view, view1, success_view, contact_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view1, name='contact'),  # Home view,
    path('success/', success_view, name='success'),
    path('contacts/', contact_list_view, name='contact_list'),
    path('contacts/delete/<int:pk>/', delete_contact_view, name='delete_contact')
]'''

# urls.py
from django.contrib import admin
from django.urls import path
from myapp.views import delete_contact_view, view1, success_view, contact_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view1, name='contact'),
    path('success/', success_view, name='success'),
    path('contacts/', contact_list_view, name='contact_list'),
    path('contacts/delete/<int:pk>/', delete_contact_view, name='delete_contact')
]


