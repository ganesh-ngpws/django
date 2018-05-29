# from firstapp.models import AccessRecord,Topic,Webpage
# class FormName(forms.ModelForm):
#     class Meta:
#         model = Webpage
#         # model = AccessRecord
#         # model = Webpage
#         exclude = ["name"]
        # fields = "__all__"
from django import forms
from django.contrib.auth.models import User
from firstapp.models import UserProfileInfo
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio','picture')
