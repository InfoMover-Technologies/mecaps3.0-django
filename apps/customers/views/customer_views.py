from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def customer_view(request):
    print("In customer view")

    customer_id = "101"
    customer_name = "Morgan Stanley"

    context = {
        'customer_id': customer_id,
        'customer_name': customer_name,
        'customer_address': {
            "street": "Kohefiza",
            "city": "Bhopal"
        },

        "customers": [

            {
                "id": 101,
                "name": "JPMC"
            },
            {
                "id": 102,
                "name": "Morgan Stanley"
            },
            {
                "id": 103,
                "name": "Wipro"
            }
        ]
    }

    return render(request, 'customers.html', context, status=200)
