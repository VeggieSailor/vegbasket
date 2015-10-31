from django import forms
from django.contrib.auth.models import User

#class RegisterSetupForm(forms.ModelForm):
    #username = forms.CharField(label='Username', max_length=30)
    #email = forms.EmailField(label='Username', max_length=30, required=False)
    #password = forms.CharField(widget=forms.PasswordInput(), required=False)
    #password_confirmation = forms.CharField(widget=forms.PasswordInput(), required=False)
    #def clean_password(self):
        #password = self.cleaned_data.get('password')
        #print (self.cleaned_data)
        #if len(password) < 8:
            #raise forms.ValidationError("Password must be at least 8 chars.")
        #return password
    
    #def clean_password_confirmation(self):
        #password_confirmation = self.cleaned_data.get('password_confirmation')
        #if len(password_confirmation) < 8:
            #raise forms.ValidationError("Password Confirmation must be at least 8 chars.")
        #return password_confirmation      

    #class Meta:
        #model = User
    
class UsernameSetupForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=30)
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(u'Username "%s" is invalid.' % username)
        return username
    
    class Meta:
        model = User
        fields = ("username", )