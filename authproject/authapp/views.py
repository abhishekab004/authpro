from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .utils import TokenGenerator,generate_token
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout



# Create your views here.

def signup(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        confirm_password=request.POST.get('pass2')
        if password != confirm_password :
            # return HttpResponse ("Incorrect Password please provide valid password")
            messages.error(request,"Password is not matching !!!")
            return render(request,'authentication/signup.html')
        try:
            if User.objects.get(username=email):
                # return HttpResponse('Email already exist')
                messages.error(request,"Email is already used !!!")
                return render(request,'authentication/signup.html')

        except Exception as identifier: 
            pass

        user= User.objects.create_user(email,email,password)
        user.is_active=False
        user.save()
        email_subject='Activate Your account'
        message=render_to_string('authentication/activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
        })
        email_message= EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
        email_message.send()
        messages.success(request,'Activate Your account by clicking the link in your gmail')
        return redirect('/auth/login/')
    return render(request,'authentication/signup.html')

class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_text(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"account activated successfully")
            return redirect('/auth/login')
        return render(request,'authentication/activatefail.html')


def handlelogin(request):
    if request.method=='POST':
        username= request.POST.get('email')
        userpassword= request.POST.get('pass2')
        myuser= authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successfull")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/auth/login/')
    return render(request,'authentication/login.html')

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Successfull")
    return redirect('/auth/login')
 