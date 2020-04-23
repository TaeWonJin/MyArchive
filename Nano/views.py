from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'main.html')

def dict(request):
    return render(request,'dict.html')

def exam(request):
    return render(request,'exam.html')

def des(request):
    return render(request,'description.html')
    
def summary(request):
    return render(request,'summary.html')