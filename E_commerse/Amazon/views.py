from django.shortcuts import render
from Amazon.models import Product



# Create your views here.

def index(request):
    accessories=Product.objects.all()
    return render(request,'index.html',{'laptop':accessories})
