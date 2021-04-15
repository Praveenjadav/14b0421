from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def view1(request):
    return HttpResponse("<h1>Helllo world</h1>")

def view2(request):
    return render(request,"view2.html",context={'email':"venu@gmail.com",'name':"Akshay"})

def view3(request,name):
    return HttpResponse(f'<h1>Hello mr./ms. {name}</h1>')

def if_demo(request):
    login=True
    return render(request,"ifelse_demo.html",context={'login':login})

def ifelse_demo(request):
    login=True
    return render(request,"ifelse_demo.html",context={'login':login,'name':'Akshay','a':10, 'b':50})

def for_demo(request):
     return render(request,"for_demo.html",context={"items":['apple','ball','cat'],'profile':{'name':"akshay","age":27,"sal":10}})
