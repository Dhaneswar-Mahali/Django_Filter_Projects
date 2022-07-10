from django import forms

class UserRegisterForm(forms.Form):
    username = forms.CharField(
        label='Your Name',
        widget=forms.TextInput(
            attrs= {
                'class' : 'form-control',
                'placeholder': 'UserName',
            }
        )
    )

    first_name = forms.CharField(
        label='Your FirstName',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'FirstName',
            }
        )
    )

    last_name = forms.CharField(
        label='Your LastName',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'LastName',
            }
        )
    )

    email = forms.EmailField(
        label='Your Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Yourname@gmail.com',
            }
        )
    )

    password1 = forms.CharField(
        label='Enter Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'password',
            }
        )
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'confirm password',
            }
        )
    )

class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'UserName',
            }
        )
    )
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )