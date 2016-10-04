from django import forms
from artist.models import Artist
from django.contrib.auth import get_user_model

User=get_user_model()

class UserForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput,label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput,label='Confirm Password')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')

        if email != email2:
            raise forms.ValidationError("Emails must match")
        if password != password2:
            raise forms.ValidationError("Passwords must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")

        return super(UserForm,self).clean(*args, **kwargs)

    # def clean_email2(self):
    #     email = self.cleaned_data.get('email')
    #     email2 = self.cleaned_data.get('email2')
    #     if email != email2:
    #         raise forms.ValidationError("Emails must match")
    #     email_qs = User.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError("This email has already been registered")
    #     return email


class ArtistForm(forms.ModelForm):
    image=forms.ImageField(label='Upload Picture')
    class Meta:
        model = Artist
        exclude = ['user','listens','loved']


    def save(self, for_user):
        self.instance.user = for_user
        return super().save()