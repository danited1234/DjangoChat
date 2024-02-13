from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
    

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'w-full mt-2 px-4 py-2 rounded-xl'})
        self.fields['password'].widget.attrs.update({'class': 'w-full mt-2 px-4 py-2 rounded-xl'})

