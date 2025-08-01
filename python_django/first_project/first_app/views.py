from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
# Create your views here.

def index(request):
    # return HttpResponse("Hello World!")
    webpages_list = AccessRecord.objects.order_by('date') #Order by date column in AccessRecord table
    date_dict= {'access_records':webpages_list}
    my_dict = {'insert_me':"Hello I am from views.py"} # This is for inserting this content in the html page index.html
    
    return render(request,'first_app/index.html',context=date_dict)
    #Render HTML page with the given context, In this case a dictionary
    #Notes:Think of the context parameter as a way to pass data from your view function to your template, 
    #      allowing you to dynamically generate HTML content based on the data.