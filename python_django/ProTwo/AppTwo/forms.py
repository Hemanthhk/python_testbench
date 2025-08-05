from django import forms
from appTwo.models import User

class NewUserForm(forms.ModelForm):

    class Meta():
        model = User #creating a model for the User
        fields = '__all__'
