from django.shortcuts import render
from django.http import HttpResponse
import requests as req
def get_data(request):
   url = request.POST.get("url")
   if "ip.me" in url:
      response = req.get(url,data="flag=TVUCTF{He110-wh0-4r3-y0u?}")
      if len(response.text) < 19:
         return HttpResponse(response.text,"txt",200)
      else:
         return HttpResponse("response Big","txt",200)
         
   else:
      return HttpResponse("\"ip.me\" must be used","txt",403)
   


def index(request):
   return render(request,"index.html",{"response":""})