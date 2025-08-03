from django import forms
from django.core import validators

def check_for_z(value):
    """
    Custom method for a speific field validation
    """
    if value[0].lower()!='z':
        raise forms.ValidationError("NOTE: Name needs to start with z!")

class FormPage(forms.Form):
    
    # name = forms.CharField(max_length=100, validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:') # Validation email field, Need to enter twice.
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    # NOTE: botcatcher checks if there are any changes in the input tag to prevent spam bots from submitting the form.
    # Here bots are assumed to modify the input tag of html rather than click normally on submit button like humans

    def clean(self):
        """
        super().clean() calls the parent class's clean() method to run the built-in validation and gather all the cleaned (validated) data from the individual fields.
        """
        all_clean_data = super().clean() #super().clean() returns a dictionary called cleaned_data. This contains key-value pairs for all fields that passed validation.
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email!=vemail:
            raise forms.ValidationError("Emails do not match!")


    