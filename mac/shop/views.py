from django.shortcuts import render
from .models import Product,Contact
from math import ceil


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
    return render(request, 'shop/tracker.html')


def checkout(request):
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
    return render(request, 'shop/contact.html')

def about(request):
    return render(request, 'shop/about.html')


def buy(request):
    return render(request, 'shop/buy.html')
