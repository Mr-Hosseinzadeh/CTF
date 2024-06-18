from django.db import IntegrityError, connection
from django.shortcuts import render,redirect
from .models import Member
from django.contrib.auth.hashers import make_password


def register(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
   
    new_user = Member(username=username, password=password)
    try:
        new_user.save()
        return render(request,"dashboard.html",context={"name":username,"success":True})
    except IntegrityError:
        return render(request,"dashboard.html",context={"name":"Registration failed","success":False})
        
        
def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    sql_injection = "/*" in username or "--" in username or "#" in username or  "/*" in password or "--" in password or "#" in password or "=" in username or "=" in password
    if sql_injection:
        return render(request,"dashboard.html",context={"name":"SQL Injection","success":False})
    query = f"Select * From members where username='{username}' AND password='{password}'"
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result)>0:
            username = result[0][1]
            if username == "admin":
                return render(request,"dashboard.html",context={"name":username,"success":True,"flag":"TVUCTF{1nj3c710n5-3n61n33r}"})
            else:
                return render(request,"dashboard.html",context={"name":username,"success":True,"flag":"null"})
        return render(request,"dashboard.html",context={"name":"The username or password is incorrect","success":False})
    
    
def index(request):
    return render(request, 'index.html')
