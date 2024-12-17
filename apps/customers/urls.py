from django.urls import path

from apps.customers.views.customer_views import customer_view

urlpatterns = [

    path('', customer_view, name="customer_view"),
]
