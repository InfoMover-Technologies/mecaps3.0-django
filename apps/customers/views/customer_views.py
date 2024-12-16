from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def customer_view(request):
    print("In customer view")
    return render(request, 'customers.html', status=200)
