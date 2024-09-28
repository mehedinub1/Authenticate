from django.shortcuts import redirect,render
from myapp.models import*
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required
def master(req):
    return render(req,"master.html")
def registerpage(req):
    if req.method=='POST':
        username=req.POST.get('username')
        email=req.POST.get('email')
        usertype=req.POST.get('usertype')
        
        password=req.POST.get('password')
        confirm_password=req.POST.get('confirm_password')
        if password==confirm_password:
            user=CustomUser.objects.create_user(
                 username=username,
                 email=email,
                 usertype=usertype,
                 
                 password=password, 
            )
            return redirect('loginpage')
        
    return render(req,"registerpage.html")
def loginpage(req):
     if req.method=='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        user=authenticate(
            
            username=username,
            password=password,   
        )
        if user:
            login(req,user)
            return redirect('master')
        
    
     return render(req,"loginpage.html")
def logoutpage(req):
    logout(req)
    
    
    return redirect('loginpage')
def profilepage(req):
    return render(req,"profilepage.html")
def createrusume(req):
    return render(req,"createrusume.html")

