from django import forms

class NewsletterForm(forms.Form):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'newsletter-input',   # Clase CSS
            'placeholder': 'Introduce tu correo'
        })
    )
