from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apps.customers.model.customer import Customer


@csrf_exempt
def customer_view(request):
    print("In customer view")

    customer_id = "101"
    customer_name = "Morgan Stanley"

    customers = Customer.objects.all()
    # Convert documents to dictionaries with renamed id field
    customer_list = [{
        'id': str(customer._id),  # rename _id to id
        'name': customer.name,
        # other fields...
    } for customer in customers]

    context = {
        'customer_id': customer_id,
        'customer_name': customer_name,
        'customer_address': {
            "street": "Kohefiza",
            "city": "Bhopal"
        },

        "customers" : customer_list
        # "customers": [
        #
        #     {
        #         "id": 101,
        #         "name": "JPMC"
        #     },
        #     {
        #         "id": 102,
        #         "name": "Morgan Stanley"
        #     },
        #     {
        #         "id": 103,
        #         "name": "Wipro"
        #     }
        # ]
    }

    return render(request, 'customers.html', context, status=200)
