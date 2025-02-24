from django import forms

from user.models import Account


class AccountAdminForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'user', 'status']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'input input-bordered w-full mb-4 rounded', 'style': 'color: #000;'}),
            'user': forms.Select(
                attrs={'class': 'input input-bordered w-full mb-4 rounded', 'style': 'color: #000;'}),
            'status': forms.Select(
                attrs={'class': 'input input-bordered w-full mb-4 rounded', 'style': 'color: #000;'})
        }
