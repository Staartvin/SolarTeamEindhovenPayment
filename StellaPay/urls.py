"""StellaPay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from .views import identification, users, products, transactions

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('identification/request-user/<str:card_id>/', identification.check_identification),
    path('identification/add-card-mapping/', identification.generate_card_mapping),
    path('users', users.get_users),
    path('products', products.get_products),
    path('products/product/<str:product_name>', products.get_product_info),
    path('transactions/user', transactions.get_transactions),
]
