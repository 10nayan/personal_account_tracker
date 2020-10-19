from django.forms import ModelForm
from .models import Report
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=("username", "email","first_name","last_name","password1","password2")
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control','placeholder':'Type your name','label':None})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Type your email'})
        self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':'Type your first name'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'Type your last name'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Enter your password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Enter your password again'})
class ReportForm(ModelForm):
    class Meta:
        model=Report
        fields=('description','cost','date','tags')
    