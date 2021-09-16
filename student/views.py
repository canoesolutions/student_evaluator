import csv, io
from django.shortcuts import redirect, render
from .models import Emotional_Intelligence, Intellectual_Capacity, Meta_Cognitive_Test, Personal_Test, Student_Details
from django.contrib import messages
from datetime import date, datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

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

#This Function will redirect to the Upload Page
def upload(request):
    return render(request, "upload.html")





############################################################
# This Function will Upload Emotional Intelligence csv file
def uploadei(request):
    data = Student_Details.objects.all()
    
    prompt = {
        'order': 'Please check the order of the coloumns in sheet' ,
        'profiles': data 
              }

    if request.method == "GET":
        return render(request, "upload.html", prompt)


    #Emotional Intelligence Upload
    csv_file = request.FILES['iefile']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A SUPPORTED FILE')

    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        try:
            student = Student_Details.objects.get(email_id=column[10].strip())
        except:
            student = None
        
        stud = None
        if student == None:

            created = Student_Details.objects.create(
            
                first_name = column[1],
                middle_name = column[2],
                last_name = column[3],
                gender = column[4],
                age = column[5],
                college_name = column[6],
                student_year = column[7],
                branch_name = column[8],
                mobile_number = column[9],
                email_id = column[10],
                hometown = column[11],
            )
            stud = created
        else:
            stud = student
        createie = Emotional_Intelligence.objects.update_or_create(
                student_id = stud,
                self_awareness = column[12],
                self_management = column[13],
                social_awareness = column[14],
                social_skills = column[15],
                emotional_intelligence = column[16],
                emotional_quotient = column[17],
                eitest_date = column[18],
                
            )

    context = {}
    return render(request, "upload.html", context)





##########################################################
#This Function will  Upload Intellectual Capacity csv File 
def uploadic(request):
    data = Student_Details.objects.all()
    
    prompt = {
        'order': 'Please check the order of the coloumns in sheet' ,
        'profiles': data 
              }

    if request.method == "GET":
        return render(request, "upload.html", prompt)


    #Intellectual Capacity Upload
    csv_file = request.FILES['icfile']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A SUPPORTED FILE')

    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        try:
            student = Student_Details.objects.get(email_id=column[10].strip())
        except:
            student = None
        
        stud = None
        if student == None:

            created = Student_Details.objects.create(
            
                first_name = column[1],
                middle_name = column[2],
                last_name = column[3],
                gender = column[4],
                age = column[5],
                college_name = column[6],
                student_year = column[7],
                branch_name = column[8],
                mobile_number = column[9],
                email_id = column[10],
                hometown = column[11],
            )
            stud = created
        else:
            stud = student
        creatic = Intellectual_Capacity.objects.update_or_create(
                student_id = stud,
                clear_thinking = column[12],
                observational_ability = column[13],
                reasoning_ability = column[14],
                critical_reasoning = column[15],
                abstract_reasoning = column[16],
                intelligence_quotient = column[17],
                ictest_date = column[18],
                
            )

    context = {}
    return render(request, "upload.html", context)




def about(request):
    return render(request, 'about.html')


########################################
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