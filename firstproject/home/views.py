from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse
from home.forms import StudentForm
from home.models import Student2, Student
from django.db.models import Q

# Create your views here.

def index(request):
    # names = ['Fruit', 'Apple', 'ABC']
    # context = {
    #     "names": names,
    #     "fruits": None,
    # }

    context = {'form': StudentForm}

    if request.method == 'POST':
        # data = StudentForm(request.POST)
        # HTML forms
        name = request.POST.get('full-name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        file = request.FILES['file']

        Student2.objects.create(name=name, age=age, gender=gender, file=file)
        print(file)

        print(name, age, gender)

        return redirect('/thank-you/')

        # if data.is_valid():

        #     # name = data.cleaned_data['name']
        #     # age = data.cleaned_data['age']
        #     # Student2.objects.create(name=name, age=age)

        #     # or
        #     # data.save()
        #     return redirect('/thank-you/')
    else:
        print(request.method)
    return render(request, 'index.html', context)

def thank_you(request):
    return HttpResponse('Thank You. Your response is recorded.')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def dynamic_route(request, number):
    return HttpResponse(f"Dynamic route by number {number}")


# Django Lookups
def search_page(request):
    students = Student.objects.all()
    

    search = request.GET.get('search')
    age = request.GET.get('age')
    if search:
        # name__icontains => lookup method (if there is name == search get that row)
        # students = students.filter(name__icontains = search)
        # students = students.filter(email__icontains = search)
        
        # For foreign key
        # students = students.filter(college__college_name__icontains = search)


        # for multi search
        students = students.filter(
            Q(name__icontains = search) |
            Q(email__icontains = search) | 
            Q(mobile_number__icontains = search) | 
            Q(gender__icontains = search)
        )

    if age:
        if age == "1":
            students = students.filter(age__gte = 18, age__lte = 20).order_by('age')
        
        if age == "2":
            students = students.filter(age__gte = 20, age__lte = 22).order_by('age')

        if age == "3":
            students = students.filter(age__gte = 22, age__lte = 24).order_by('age')
    
    context = {
        'students':students,
        'search':search
    }
    return render(request, 'search.html', context)