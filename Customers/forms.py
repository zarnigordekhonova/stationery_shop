from django import forms
from Customers.models import CustomUser
from django.core.exceptions import ValidationError


class CustomUserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'image']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


    def clean_password2(self):
        cd = self.cleaned_data

        if cd.get('password') != cd.get('password2'):
            raise ValidationError("Passwords do not match.")

        return cd['password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'image', 'email')