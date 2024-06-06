from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm): 
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    
    
    class Meta:     #We use the Meta class to specify metadata about the form.
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):             #__init__ method to customize the form's initialization.
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password2'].help_text = "Enter the same password as before, for verification."    
        
        #This addition provides a clear hint to users about the purpose of the password2 field.