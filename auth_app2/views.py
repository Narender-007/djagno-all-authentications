from django.shortcuts import render
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def success(request):
    return render(request, "success.html")


def logout_view(request):
    logout(request)
    return redirect('/')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        creationForm = CustomUserCreationForm(request.POST)
        if creationForm.is_valid():
            creationForm.save()
            return redirect("login")
        else:
            form = CustomUserCreationForm()
            return render(request, "index.html", { "form":form})
    else:
        form = CustomUserCreationForm()
        return render(request, "index.html", { "form":form})
    
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a success page (change 'home' to your desired URL name)
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})
    
@login_required
def home(request):
    return render(request, "home.html")


            
            
    
