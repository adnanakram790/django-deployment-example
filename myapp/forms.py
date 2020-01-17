from django import forms
from myapp.model import Signup,Login
# from django.core import validators
# from django.core.validators import RegexValidator
# # # Create your views here.
# class New(forms.ModelForm):
#     class Meta():
#         model = FormName
#         # fields = '__all__'
#         fields = ('name','email','password','portfolio_site','picture')

class Signu(forms.ModelForm):
    class Meta():
        model = Signup
        fields = '__all__'
        
# class Logi(forms.ModelForm):
#     class Meta():
#         model = Login
#         field = ('email1','password1')

class New1(forms.ModelForm):
    class Meta():
        model = Login
        fields = '__all__'


# alphanum=RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

# alphanum1=RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')


# class FormName(forms.Form):
#     name = forms.CharField(max_length=50,validators=[alphanum])
#     email = forms.EmailField()
#     password = forms.CharField(max_length=50,validators=[alphanum1])

#     # text = forms.CharField(widget=forms.Textarea)
# class Log(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(max_length=50,validators=[alphanum1])