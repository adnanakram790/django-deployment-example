from django.db import models
from django.core import validators
from django.core.validators import RegexValidator


# Create your views here.

alphanum=RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

alphanum1=RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')
class Signup(models.Model):
    name = models.CharField(max_length=50,validators=[alphanum])
    email = models.EmailField()
    password = models.CharField(max_length=50,validators=[alphanum])
    portfolio_site = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics' , blank=True)
class Login(models.Model):
    email1= models.EmailField()
    password1 = models.CharField(max_length=50,validators=[alphanum] )







# class FormName(models.Model):
#     #   name=models.OneToOneField(User)
#     name = models.CharField(max_length=50,validators=[alphanum])
#     email = models.EmailField()
#     password = models.CharField(max_length=50)
#     portfolio_site = models.URLField(blank=True)
#     picture = models.ImageField(upload_to='profile_pics',blank= True)

# class Signup(models.Model):
#  #     name=models.OneToOneField(User)
#     name = models.CharField(max_length=50,validators=[alphanum])
#     email = models.EmailField()
#     password = models.CharField(max_length=50)
#     portfolio_site = models.URLField(blank=True)
#     picture = models.ImageField(upload_to='profile_pics',blank= True)



#     # text = forms.CharField(widget=forms.Textarea)
# class Log(models.Model):
#     email = models.EmailField()
#     password = models.CharField(max_length=50,validators=[alphanum1])



# class Recipe(models.Model):
#     name =models.CharField(max_length=50,validators=[alphanum])
#     category = models.CharField(max_length=50,validators=[alphanum1])
#     rating =models.DecimalField(max_digits=2,max_length=5, decimal_places=None,validators=())


