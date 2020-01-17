from django.shortcuts import render
# from myapp.model import FormName,Log  
# from django.core import validators
# from django.core.validators import RegexValidator
from myapp.forms import Signu,New1

def index(request):
    return render(request,'index.html')
    
def signup(request):
    form=Signu()
    if request.method=='POST':
        form=Signu(request.POST)

        if form.is_valid:
            # print("validation success")
            # print("UserName:"+form.cleaned_data['name'])
            # print("Email:"+form.cleaned_data['email'])
            # print("Password:"+form.cleaned_data['password'])
            # print("textarea:"+form.cleaned_data['text'])
            form.save(commit=True)
            return index(request)
        else:
            print("Invalid Error")
    
    
    return render(request,'signup.html',{'form':form})
def login(request):
    form=New1()
    if request.method=='POST':
        form=New1(request.POST)

        if form.is_valid:
            # print("validation success")
            # print("UserName:"+form.cleaned_data['name'])
            # print("Email:"+form.cleaned_data['email'])
            # print("Password:"+form.cleaned_data['password'])
            # print("textarea:"+form.cleaned_data['text'])
            form.save(commit=True)
            return index(request)
        else:
            print("Invalid Error")
    
    
    return render(request,'signup.html',{'form':form})
def otherfile(request):
    return render(request,'otherfile.html')
def base(request):
    return render(request,'base.html')
def about(request):
    return render(request,'about.html')
















# def index(request):
#      return render(request,'index.html')
# def signup(request):
#     form=forms.FormName()
#     if request.method=='POST':
#         form=forms.FormName(request.POST)

#         if form.is_valid():
#             print("validation success")
#             print("UserName:"+form.cleaned_data['name'])
#             print("Email:"+form.cleaned_data['email'])
#             print("Password:"+form.cleaned_data['password'])
#             # print("textarea:"+form.cleaned_data['text'])

#     return render(request,'signup.html',{'form':form})
# def login(request):
   
#     form=forms.Log()
#     if request.method=='POST':
#         form=forms.Log(request.POST) 

#         if form.is_valid():
#             print("validation success")
#             print("Email:"+form.cleaned_data['email'])
#             print("Password:"+form.cleaned_data['password'])
#             # print("textarea:"+form.cleaned_data['text'])

#     return render(request,'login.html',{'form':form})
