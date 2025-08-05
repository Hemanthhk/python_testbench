from django.urls import path
from basic_app import views

#TEMPLATE_TAGGING
app_name = 'basic_app' # Django will look into this in templates, if relative url is used. This needs to match in the templates, {% url app_name:template_name%}

urlpatterns= [
    path('relative/',views.relative,name= 'relative'),
    path('other/',views.other,name='other')

]