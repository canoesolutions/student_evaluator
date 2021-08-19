import csv, io
from django.shortcuts import render, HttpResponse
from .models import Student_Details
from django.contrib import messages
from datetime import date, datetime

# Create your views here.
def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def upload(request):

    template = "upload.html"
    data = Student_Details.objects.all()
    
    prompt = {
        'order': 'Please check the order of the coloumns in sheet' ,
        'profiles': data 
              }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A SUPPORTED FILE')

    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Student_Details.objects.update_or_create(
            
            first_name = column[0],
            middle_name = column[1],
            last_name = column[2],
            gender = column[3],
            age = column[4],
            college_name = column[5],
            student_year = column[6],
            branch_name = column[7],
            mobile_number = column[8],
            email_id = column[9],
            hometown = column[10],
            test_date = column[11],
        )

    context = {}
    return render(request, template, context)
   

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def report(request):
    return render(request, 'report.html')
