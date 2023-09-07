from django import forms

class ConfigForms(forms.Form):
    address = forms.CharField(
        widget=forms.TextInput(attrs={"class": "rounded-lg mt-2 w-full", "placeholder": "ex : 192.168.x.x"})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "rounded-lg mt-2 w-full", "placeholder": "ex : admin"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "rounded-lg mt-2 w-full"})
    )
    config = forms.CharField(

        required=True,

        widget=forms.widgets.Textarea(

            attrs={

                "placeholder": "masukan konfigurasi",

                "class": "rounded-lg mt-3",

            }

        ),

        label="Konfigurasi",

    )