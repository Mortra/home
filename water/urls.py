"""water URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from core.views import *
from clients.views import *
from django.conf import settings
from django.conf.urls.static import static
from clients import forms




urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', clients_list),
    path('contacts/', contacts),
    path('about/', about),
    path('makers/', makers_list),
    path('photo/', photo, name="client-create"),
    path('clients/', clients_list, name="client-list"),
    path('client/<int:id>/', client_detail, name="client-detail"),
    path('bottle/', bottle_list, name="bottle-list"),
    path('bottle/<int:id>/', bottle_detail, name="bottle-detail"),
    path('order/create/', create_order, name="create-order"),
    path('order/djangoform/', order_djangoform, name="order-djangoform"),
    path('order/', order_list, name="order-list"),
    path('order/<int:id>/', order_detail, name="order-detail"),
    path('<int:pk>/delete', forms.DeleteUpdateView.as_view(), name='client-delete'),
    path('<int:pk>/update', forms.ClientUpdateView.as_view(), name='update-delete')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
