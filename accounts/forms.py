from django import forms
from accounts.models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("vehicle", "caption", "image")


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'username', 'address', 'mobile', 'city', 'state', 'agreed_to_terms']

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last name"}),
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "address": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter your address", "rows": 3}),
            "mobile": forms.TextInput(attrs={"class": "form-control", "placeholder": "Mobile number"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
            "state": forms.TextInput(attrs={"class": "form-control", "placeholder": "state"}),
            "agreed_to_terms": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    username = forms.EmailField(label="Email")

    mobile = forms.CharField(max_length=15)

    def clean_mobile(self):
        mobile = self.cleaned_data.get("mobile")
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Enter a valid 10-digit mobile number.")
        return mobile
    
    