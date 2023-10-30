from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        labels = {
            'stname': 'STORE NAME',
            'phno': 'PHONE NUMBER',
            'email': 'EMAIL',
            'add': 'ADDRESS'
        }

        widgets = {
            'stname': forms.DateInput(attrs={'placeholder': 'eg. Gucci'}),
            'add': forms.Textarea(attrs={'placeholder': 'eg. JM ROAD PUNE'}),
            'phno': forms.DateInput(attrs={'placeholder': 'eg. 9486327751'}),
            'email': forms.EmailInput(attrs={'placeholder': 'eg. gucci@.com'})
        }
