from django import forms
from django.contrib.auth.forms import AuthenticationForm

from guanxi_app.user.models import User


class CustomAuthenticationForm(AuthenticationForm):
    # Redefinindo o campo username para email, pois usamos email para login
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-3 py-2 border rounded dark:bg-gray-600 dark:text-black text-black hover:text-black',
            'placeholder': 'Seu email',
            'style': 'color: #000;'
        }),
        label="Email"
    )
    # O campo password herda os atributos definidos no form original.
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border rounded dark:bg-gray-600 dark:text-black text-black hover:text-black',
            'placeholder': 'Sua senha',
            'style': 'color: #000;'
        }),
        label="Senha"
    )


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border rounded dark:bg-gray-600 dark:text-black text-black hover:text-black',
            'placeholder': 'Senha',
            'style': 'color: #000;'
        })
    )
    password2 = forms.CharField(
        label="Confirmar Senha",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border rounded dark:bg-gray-600 dark:text-black text-black hover:text-black',
            'placeholder': 'Confirme sua senha',
            'style': 'color: #000;'
        })
    )

    class Meta:
        model = User
        fields = ('email', 'cpf', 'contact', 'first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded dark:bg-gray-600 dark:text-black text-black hover:text-black',
                'placeholder': 'Seu nome',
                'style': 'color: #000;'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded dark:bg-gray-600 dark:text-black text-black hover:text-black',
                'placeholder': 'Seu último nome',
                'style': 'color: #000;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-3 py-2 border rounded dark:bg-gray-600 dark:text-black text-black hover:text-black',
                'placeholder': 'Seu email',
                'style': 'color: #000;'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded dark:bg-gray-600 dark:text-black text-black hover:text-black',
                'placeholder': 'Seu CPF',
                'style': 'color: #000;'
            }),
            'contact': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded dark:bg-gray-600 dark:text-black text-black hover:text-black',
                'placeholder': 'Contato',
                'style': 'color: #000;'
            }),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não conferem.")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
