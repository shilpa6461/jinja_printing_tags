from django.shortcuts import render

# Create your views here.

def wish(request):
    d={'name':'OOHA','age':11,'marks':90}
    return render(request,'wish.html',context=d)
