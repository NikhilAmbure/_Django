from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse
from home.forms import StudentForm
from home.models import Student2

# Create your views here.

def index(request):
    # names = ['Fruit', 'Apple', 'ABC']
    # context = {
    #     "names": names,
    #     "fruits": None,
    # }

    context = {'form': StudentForm}

    if request.method == 'POST':
        data = StudentForm(request.POST)
        if data.is_valid():
            name = data.cleaned_data['name']
            age = data.cleaned_data['age']
            Student2.objects.create(name=name, age=age)

            return redirect('/thank-you/')
    else:
        print(request.method)
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def dynamic_route(request, number):
    return HttpResponse(f"Dynamic route by number {number}")

def thank_you(request):
    return HttpResponse('Thank You. Your response is recorded.')