from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json
import datetime


def index(request):
    product = Product.objects.all()
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for item in cats:
        prod = Product.objects.filter(category=item)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nslides), nslides])
    params = {'allprods': allprods}
    return render(request, 'shop/index.html', params)



def tracker(request):
    if request.method == "POST":
        orderid = request.POST.get('orderid', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderid, email=email)
            if len(order) > 0:
                Update = OrderUpdate.objects.filter(order_id=orderid)
                updates = []
                for item in Update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("No Data Found")
        except Exception as e:
            return HttpResponse(e)

    return render(request, 'shop/tracker.html')


def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        json_item = request.POST.get('json_item', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        phone = request.POST.get('phone', '')
        zip_code = request.POST.get('zip_code', '')

        orders = Orders(json_item=json_item, email=email, name=name, phone=phone, address=address, city=city,
                        zip_code=zip_code, state=state)

        orders.save()
        update = OrderUpdate(order_id=orders.order_id, update_desc="The Order Has been Palced")
        update.save()
        thank = True
        id = orders.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')


def proview(request, myid):
    # Fethch the data from product using id
    products = Product.objects.filter(id=myid)
    param = {'product': products[0]}
    return render(request, 'shop/proview.html', param)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(c_name=name, c_email=email, c_phone=phone, c_desc=desc)
        contact.save()
        thank = True
        return render(request, 'shop/contact.html', {'thank': thank})
    return render(request, 'shop/contact.html')


def about(request):
    return render(request, 'shop/about.html')


def buy(request):
    return render(request, 'shop/buy.html')
