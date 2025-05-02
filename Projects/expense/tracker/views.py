from django.shortcuts import render, redirect
from django.contrib import messages
from tracker.models import Transaction
from django.db.models import Sum, Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# User Authentication
def registration(request):
    if request.method == 'POST':
        first_name  = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')
        username  = request.POST.get('username')
        email  = request.POST.get('email')
        password  = request.POST.get('password')

        
        # If username or email already exists
        user_obj = User.objects.filter(
            Q(email = email) |  Q(username = username)
            )

        if user_obj.exists():
            messages.error(request, "Username or Email Already Exist")
            return redirect('/registration/')
        

        # You cannot pass the password here because it is encrypted
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email
        )

        # To pass the password
        user.set_password(password)
        user.save()
        messages.error(request, 'Success : Account Created')
        return redirect('/registration/')


    return render(request, 'registration.html')


# Login logic
def LoginPage(request):
    if request.method == 'POST':
        username  = request.POST.get('username')
        password  = request.POST.get('password')

        user_obj = User.objects.filter(username = username)

        # To check whether the user exists or not
        if not user_obj.exists():
            messages.error(request, 'Error: User does not exists')
            return redirect('/login/')


        # whether the username and password matches or not
        # if does not matches 'authenticate' returns None
        user_obj = authenticate(username = username, password = password)

        if not user_obj:
            messages.error(request, 'Error: Invalid Crendentials')
            return redirect('/login/')

        
        login(request, user_obj)
        return redirect('/')
    
    return render(request, 'login.html')


# Logout Logic
def LogoutPage(request):
    logout(request)
    messages.error(request, 'Success: Logged out successfully.')
    return redirect('/login/')


def index(request):

    # To check whether user is authenticated
    print(request.user)

    if request.method == "POST":
        description = request.POST.get('description')
        amount = request.POST.get('amount')

        if description is None:
            messages.info(request, "Description cannot be blank")
            return redirect('/')

        try:
            amount = float(amount)
        except Exception as e:
            messages.info(request, "Should be a Number")
            return redirect('/')
        
        Transaction.objects.create(amount=amount, description=description)

        return redirect('/')
    
    context = {'transactions': Transaction.objects.all(),
               'balance': Transaction.objects.all().aggregate(total_balance = Sum('amount'))['total_balance'] or 0,
               'income' : Transaction.objects.filter(amount__gte = 0).aggregate(income = Sum('amount'))['income'] or 0,
               'expense': Transaction.objects.filter(amount__lte = 0).aggregate(expense = Sum('amount'))['expense'] or 0,
               }
    return render(request, "index.html", context)


def delTransaction(request, uuid):
    Transaction.objects.get(uuid = uuid).delete()
    return redirect('/')