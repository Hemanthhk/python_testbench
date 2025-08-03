from django.shortcuts import render
# from django.http import request
from basicapp import forms
# Create your views here.

def index(request):
    return render(request,'basicapp_templates/index.html')

def form_view(request):
    form = forms.FormPage() # Create a FormPage object
    #If someone is posted any data and the form is valid
    if request.method == 'POST':
        form = forms.FormPage(request.POST) #Get the POSTed data to the form page
        
        if form.is_valid():
            #Do something is user enters some data
            print("name: " +form.cleaned_data['name'])
            print("email: "+form.cleaned_data['email'])
            print("text: "+form.cleaned_data['text'])

    return render(request,'basicapp_templates/form_page.html', context= {'form':form})