from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.


def index(request):
    if request.user.is_authenticate:
        return render(request,'home.html')
    else:
        return redirect('/login')

def signout(request):
    logout(request)
    return redirect('/login')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST': 
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save() # save the user

            # login this new user
            user_name = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username = user_name, password = password)
            login_user(request, user)
            return redirect('/')

        else:
            # form not valid
            return render(request, 'signup.html', {'form': form })

    else:
        # not post = GET
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form })


def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST': 
        # validate credential
        user_name = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = user_name, password = password)

        if user is not None: 
            # valid creds
            login_user(request, user) # save the user as logged in
            return redirect('/')
        else:
            form = AuthenticationForm()
            return render(request, "login.html", {"form": form})

    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})
