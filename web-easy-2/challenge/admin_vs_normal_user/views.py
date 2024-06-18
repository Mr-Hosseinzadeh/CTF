from django.http import HttpResponse
from django.shortcuts import render
import base64 


flag = "TVUCTF{7h3-m4n463r-15-n07-w3ll}"
def index(request):
    cookie = request.COOKIES
    keys = cookie.keys()
    if 'role' in keys:
        decode = base64.b64decode(cookie["role"]).decode()
        if decode =="d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35":
            return render(request,"index.html",{"result":"The flag is on the admin page"})
        elif decode =="6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b":
            return render(request,"index.html",{"result":flag})
    else:
        response = HttpResponse("The flag is on the admin page")
        response.set_cookie("role","ZDQ3MzVlM2EyNjVlMTZlZWUwM2Y1OTcxOGI5YjVkMDMwMTljMDdkOGI2YzUxZjkwZGEzYTY2NmVlYzEzYWIzNQ==")  
        return response