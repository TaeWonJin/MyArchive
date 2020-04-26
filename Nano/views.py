from django.shortcuts import render
from .models import Descript, Images
# Create your views here.

def main(request):
    Descripts = Descript.objects.all()
    PImages = Images.objects.all()
    return render(request,'main.html',{'Descripts':Descripts,'PImages':PImages})

def dict(request):
    return render(request,'dict.html')

def exam(request):
    return render(request,'exam.html')

def des(request):
    return render(request,'description.html')
    
def summary(request):
    return render(request,'summary.html')