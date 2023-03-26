from django import forms
from .models import Contact


class AddForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'phone', 'email', 'contact_type','image','content')
        
