from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm

# Create your views here.
def front_page(request):
    return render(request,'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request,user)

            return redirect('frontpage')
    else:
        form = SignupForm()
    return render(request,'core/signup.html',{'form':form})
def logout_view(request):
    logout(request)
    return redirect('login')
class CustomLoginView(LoginView):
    template_name = 'core/login.html'  # Specify your login template
    authentication_form = LoginForm