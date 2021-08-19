import csv, io
from django.shortcuts import render, HttpResponse
from .models import Student_Details
from django.contrib import messages


# Create your views here.
def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def upload(request):

    template = "test_upload.html"
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
            student_id = column[0],
            first_name = column[1],
            last_name = column[2],
            college_name = column[3],
            branch = column[4],
            year = column[5],
            age = column[6],
            gender = column[7],
            mobile_num = column[8],
            email_id = column[9],
            hometown = column[10]
        )

    context = {}
    return render(request, template, context)
    #     student_id = request.GET.get('student_id')
    #     f_name = request.GET.get('f_name')
    #     l_name = request.GET.get('l_name')
    #     college_name = request.GET.get('college_name')
    #     branch = request.GET.get('branch')
    #     year =request.GET.get('year')
    #     age = request.GET.get('age')
    #     gender = request.GET.get('gender')
    #     mob_num = request.GET.get('mob_num')
    #     email_id = request.GET.get('email_id')
    #     hometown = request.GET.get('hometown')
    #     dob = request.GET.get('dob')
    #     test_date = request.GET.get('test_date')
    #     stu_data = Student_Details(student_id='student_id', f_name='f_name', l_name='l_name', college_name='college_name',
    #     branch='branch', year='year', age='age', gender='gender', mob_num='mob_num',email_id='email_id', hometown='hometown',
    #     dob='dob', test_date='test_date')
    #     stu_data.save()
    # return render(request, 'upload.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def report(request):
    return render(request, 'report.html')
