from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm

# Create your views here.
def homepage_view(request):
    return render(request,'testapp/home.html')

@login_required
def python_view(request):
    return render(request,'testapp/pythonexam.html')

@login_required
def java_view(request):
    return render(request,'testapp/javaexam.html')

def c_view(request):
    return render(request,'testapp/cexam.html')

def ruby_view(request):
    return render(request,'testapp/rubyexam.html')
def contact_view(request):
    return render(request,'testapp/contact.html')

def logout_view(request):
    return render(request,'testapp/logout.html')

from django.http import HttpResponseRedirect
def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
