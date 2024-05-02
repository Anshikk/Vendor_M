"""
URL configuration for vendor_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from vendors import views

urlpatterns = [
    path('', views.vendor_list),  # Root URL for accessing the list of vendors
    path('api/vendors/', views.vendor_list),
    path('api/vendors/<int:vendor_id>/', views.vendor_detail),
    path('api/purchase_orders/', views.purchase_order_list),
    path('api/purchase_orders/<int:po_id>/', views.purchase_order_detail),
    path('api/historical_performance/', views.historical_performance_list),
    path('api/historical_performance/<int:performance_id>/', views.historical_performance_detail),
]

    
