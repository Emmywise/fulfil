from celery import shared_task
from django.http.response import HttpResponse
from django.shortcuts import render
import csv, io
from .models import *
from .views import *


@shared_task
def upload_function(csv_file):

    
    # template = "item/upload-product.html"
    print("file")
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set) #loop through data to be string
    next(io_string) #skip the first line which is the header
    for colum in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Products.objects.update_or_create(
            product_name=colum[0],
            product_alert=colum[1],
            description=colum[2],
          
        )
    context = {}


    return render(request)