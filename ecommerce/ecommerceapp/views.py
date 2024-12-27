from django.shortcuts import render
from django.contrib import messages
from ecommerceapp.models import Contact,Product
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
