from django.shortcuts import render,get_object_or_404
from .models import WordDict,WordImg,SummaryImg,Summary,Solution
# Create your views here.

def main(request):

    return render(request,'main.html',)

def dict(request,pk):
    word = get_object_or_404(WordDict, pk=pk)
    wordimg = WordImg.objects.all
    return render(request,'dict.html',{'word':word,'image':wordimg})

def exam(request,pk):
    content = get_object_or_404(Solution,pk=pk)
    return render(request,'exam.html',{'content':content})
    
def summary(request,pk):
    content = get_object_or_404(Summary,pk=pk)
    summaryimg = SummaryImg.objects.all
    return render(request,'summary.html',{'content':content,'image':summaryimg})