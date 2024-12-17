from django.urls import path, include



urlpatterns = [

    # path('', include('apps.common.urls')),
    path('customers/', include('apps.customers.urls')),


]