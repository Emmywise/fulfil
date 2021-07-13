from django.shortcuts import render, redirect, get_object_or_404
import os
import csv, io
from django.contrib import messages
from .models import *
from .forms import*
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def home(request):
    return render(request, 'item/index.html') #rendering index page as home


def upload_product(request): #fucntion that fetch the datas from haflhour consumption csv file to the datbase
    template = "item/upload-product.html"
    if request.method =="GET":
        return render(request, template)
    
    # import pdb;pdb.set_trace()
    csv_file = request.FILES['file'] #get the file
    if not csv_file.name.endswith('.csv'): #check user upload only csv file format is allowed
        messages.error(request, 'This is not a csv file, upload a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set) #loop through data to be string
    next(io_string) #skip the first line which is the header
    for colum in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Products.objects.update_or_create(
            product_name=colum[0],
            product_alert=colum[1],
            quantity=colum[2],
          
        )
    context = {}
    return render(request, template, context)

def product(request):
    products = Products.objects.filter().order_by('-id')[:10]  # filter inputed data by id
    return render(request, 'item/view-product.html', {"products": products})


def register_product(request):
    if request.method == 'POST':  # making sure its a post request
        form = ProductForm(request.POST)
        if form.is_valid():  # check if data is valid
            form.save()  # save the data collect
        return HttpResponseRedirect(reverse("view-product"))  # redirect to next page after saving file
    else:
        form = ProductForm
    return render(request, 'item/register-product.html', {'form': form})

def delete_product(request, pk):
    if request.method == "POST":
        documents = Products.objects.get(pk=pk)
        documents.delete()
    return redirect('view-product')

# update view for details
def update_view(request, pk = None):
    instance = get_object_or_404(Products, pk= pk)
    form = ProductForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url()) 
    context = {
        "instance": instance,
        "form": form
    }

    return render(request, "register-product.html", context)
