from django.shortcuts import render

def student(request):
    return render(request,'index.html')