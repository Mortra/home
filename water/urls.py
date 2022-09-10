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
from django.contrib.auth.views import *
from django.urls import path, include
from core.views import *
from clients.views import *
from django.conf import settings
from django.conf.urls.static import static
from clients import forms





urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', ClientsListView.as_view()),
    path('contacts/', contacts),
    path('about/', about),
    path('', makers_list, name="makers-list"),
    path('clients/', ClientsListView.as_view(), name="client-list"),
    path('client/<int:pk>/', ClientDetailView.as_view(), name="client-detail"),
    path('bottle/', BottleListView.as_view(), name="bottle-list"),
    path('bottle/<int:pk>/', BottleDetailView.as_view(), name="bottle-detail"),
    path('order/create/', CreateOrderView.as_view(), name="create-order"),
    path('order/djangoform/', CreateOrderDjangoForm.as_view(), name="order-djangoform"),
    path('order/', OrderlistView.as_view(), name="order-list"),
    path('order/<int:pk>/', OrderDetailViews.as_view(), name="order-detail"),
    path('<int:pk>/delete', forms.DeleteUpdateView.as_view(), name='client-delete'),
    path('<int:pk>/update', forms.ClientUpdateView.as_view(), name='update-delete'),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", register, name="register")


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
