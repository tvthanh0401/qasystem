from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

# class ChangeInfoForm(UserChangeForm):
#     form_class = UserChangeForm
#     template_name = 'qa/edit_profile.html'
#     success_url = reverse_lazy('edit_profile')

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-outline mb-4'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-outline mb-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-outline mb-4'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password' )