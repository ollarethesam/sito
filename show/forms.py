# forms.py

from django import forms

class ContactForm(forms.Form):
    # Define the name field with 'Nome' as the label and the CSS class
    name = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': " "}))
    
    # Define the email field with 'Email' as the label, validation as an email field, and the CSS class
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': " "}))
    
    # Define the phone field with 'Telefono' as the label, and the CSS class
    phone = forms.CharField(label='Telefono', required=False, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': " "}))
    
    # Define the object field with 'Oggetto' as the label and the CSS class
    object = forms.CharField(label='Oggetto', max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': " "}))
    
    # Define the message field with 'Messaggio' as the label, using a Textarea widget and the CSS class
    message = forms.CharField(label='Messaggio', widget=forms.Textarea(attrs={'class': 'input-field textarea', 'placeholder': " "}))
