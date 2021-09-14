import csv, io
from django.shortcuts import redirect, render
from .models import Emotional_Intelligence, Intellectual_Capacity, Meta_Cognitive_Test, Personal_Test, Student_Details
from django.contrib import messages
from datetime import date, datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def login(request):
    return render(request, 'login.html')

# This Function will work on Index Page to calculate tests
def index(request):
    
    ei = Emotional_Intelligence.objects.all().count()
    ic = Intellectual_Capacity.objects.all().count()
    pt = Personal_Test.objects.all().count()
    mct = Meta_Cognitive_Test.objects.all().count()

    all = int(ei) + int(ic) + int(pt) + int(mct)

    context = {'all':all, 'ei':ei, 'ic':ic, 'pt':pt, 'mct':mct }

    return render(request, 'index.html', context)


# This Function will work on Search Page
def search(request):
    students = Student_Details.objects.all().order_by('first_name')
    return render(request, 'search.html',{'students':students})

# This Function will work on Uploading csv file in database
def upload(request):
    data = Student_Details.objects.all()
    
    prompt = {
        'order': 'Please check the order of the coloumns in sheet' ,
        'profiles': data 
              }

    if request.method == "GET":
        return render(request, "upload.html", prompt)

    csv_file = request.FILES['iefile']

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
        )

    context = {}
    return render(request, "upload.html", context)
   

def about(request):
    return render(request, 'about.html')


# This function will work on Report Page
def report(request, pk):
    students = Student_Details.objects.get(student_id=pk)
    try:
        ei = Emotional_Intelligence.objects.get(student_id=pk)
    except ObjectDoesNotExist:
        print("report doesn't exist")
        ei = None
    try:
        ic = Intellectual_Capacity.objects.get(student_id=pk)
    except ObjectDoesNotExist:
        print("report doesn't exist")
        ic = None
    try:
        pt = Personal_Test.objects.get(student_id=pk)
    except ObjectDoesNotExist:
        print("report doesn't exist")
        pt = None
    try:
        mct = Meta_Cognitive_Test.objects.get(student_id=pk)
    except ObjectDoesNotExist:
        print("report doesn't exist")
        mct = None
    

    context = {'students':students, 'ei':ei, 'ic':ic, 'pt':pt, 'mct':mct }
    return render(request, 'report.html', context)


# This function will Delete records on the Search Page
def delete(request, pk):
    students = Student_Details.objects.get(student_id=pk)
    students.delete()
    return redirect('/search')


# This Function will Update the Student Record on Search Page
def update(request, pk):
    students = Student_Details.objects.get(student_id=pk)
    students.save()
    return render(request, 'update.html', {'students': students})