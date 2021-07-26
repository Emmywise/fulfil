# from item.tasks import upload_function
import csv, io, os
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import ProductForm
from .models import Products


def home(request):
    return render(request, 'item/index.html')


def upload_product(request): #fucntion that fetch the datas from haflhour consumption csv file to the datbase
    template = "item/upload-product.html"
   
    if request.method =="GET":
        return render(request, template)
    
    
    csv_file = request.FILES['file'] #get the file
    if not csv_file.name.endswith('.csv'): #check user upload only csv file format is allowed
       return HttpResponse('This is not a csv file, upload a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set) #loop through data to be string
    next(io_string) #skip the first line which is the header
    for colum in csv.reader(io_string, delimiter=',', quotechar="|"):
        Products.objects.update_or_create(
            name=colum[0],
            sku=colum[1],
            description=colum[2],        
        )
    return HttpResponseRedirect(reverse("view-product"))


def product(request):
    products = Products.objects.filter().order_by('-id')  # filter inputed data by id
    return render(request, 'item/view-product.html', {"products": products})


def register_product(request):
    if request.method == 'POST':  
        form = ProductForm(request.POST)
        if form.is_valid():  
            form.save()  
        return HttpResponseRedirect(reverse("view-product"))  
    else:
        form = ProductForm
    return render(request, 'item/register-product.html', {'form': form})


 #delete product by ID
def delete_product(request, pk):
    if request.method == "POST":
        products = Products.objects.get(pk=pk)
        products.delete()
    return redirect('view-product') 


# function to delete all product
def delete_all_product(request): 
    products = Products.objects.all()
    products.delete()
    return redirect('view-product') 


# update view for product
def update_view(request, pk = None): 
    instance = get_object_or_404(Products, pk= pk)
    form = ProductForm(request.POST or None, instance = instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("view-product")
    context = {
        "instance": instance,
        "form": form
    }
    return render(request, "item/update-product.html", context)


# search product function
def search_product(request):
    query = request.GET.get('q', '')
    if query :
        products = Products.objects.filter(
            Q(name__icontains=query) | Q(sku__icontains=query)
        )
    else:
        products = Products.objects.filter().order_by('-id')[:10]  # filter inputed data by id
    return render(request, 'item/view-product.html', {"products": products})