from django.shortcuts import render
import os

def home(request):
    return render(request,"index.html")

def excute(request):
    command = request.POST.get('command')
    if command:
            result = os.popen(f"ping {command}").read()
            return render(request,"result.html",{"result":result})
    else:
        return render(request,"")
