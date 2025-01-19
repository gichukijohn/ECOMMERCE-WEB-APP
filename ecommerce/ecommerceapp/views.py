from django.shortcuts import redirect, render
from django.contrib import messages
from ecommerceapp.models import Contact, OrderUpdate, Orders,Product
from math import ceil


def index(request):
    allproducts=[]
    categoryproducts=Product.objects.values('category','id')
    categories={item['category'] for item in categoryproducts}
    for catgory in categories:
        prod=Product.objects.filter(category=catgory)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allproducts.append([prod,range(1,nSlides),nSlides])
        
    params={'allproducts':allproducts}
    return render(request,"index.html",params)

def contact(request):
    if request.method=="POST":
        name= request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        myquery=Contact(name=name,email=email,phone_number=phone,description=desc)
        myquery.save()
        messages.info(request,"we will get back soon")
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html") 


def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('login')
    if request.method=="POST":

        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        Order = Orders (items_json=items_json,name=name,amount=amount, email=email, 
                       address1=address1,address2=address2,city=city,state=state,
                       zip_code=zip_code,phone=phone)
        print(amount)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id,update_desc="the order has been placed")
        update.save()
    return render(request,"checkout.html")
