from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    response_text = "<em>My Second App</em>"
    return HttpResponse(response_text)

def help(request):
    help_dict = {'help_insert':"This is from views.py help method!"}
    return render(request,'AppTwo/help.html',context=help_dict)