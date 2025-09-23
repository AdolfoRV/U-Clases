from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, SetPasswordForm, AuthenticationForm, PasswordResetForm
)
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from .models import User
from .errors import ERROR_MESSAGES as ERR

INPUT = "w-full px-4 py-2 border border-border rounded-md bg-background text-foreground mb-2 focus:outline-none focus:ring-2 focus:ring-primary transition"

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': INPUT})
        self.fields['email'].widget.attrs.update({'class': INPUT})
        self.fields['password1'].widget.attrs.update({'class': INPUT})
        self.fields['password2'].widget.attrs.update({'class': INPUT})

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Ese email ya está registrado.")
        return email

class CustomLoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': INPUT, 'autofocus': True})
        self.fields['password'].widget.attrs.update({'class': INPUT})

class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        f = self.fields
        f['new_password1'].widget.attrs.update({'class': INPUT, 'placeholder': 'Ingresa tu nueva contraseña'})
        f['new_password2'].widget.attrs.update({'class': INPUT, 'placeholder': 'Confirma tu nueva contraseña'})

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.fields['email'].label = "Correo electrónico"
        self.fields['email'].widget.attrs.update({'class': INPUT, 'placeholder': 'tucorreo@dominio.com', 'autocomplete': 'email'})
