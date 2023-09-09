from django import forms

class ConfigForms(forms.Form):
    address = forms.CharField(
        widget=forms.TextInput(attrs={"class": "rounded-lg mt-2 w-full", "placeholder": "ex : 192.168.x.x"}),
        label= 'Ip Address'
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

class ConfigIpAddress(forms.Form):
    host = forms.CharField(
        widget=forms.TextInput(attrs={"class": "rounded-lg mt-2 w-full", "placeholder": "ex : 192.168.1.x"})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "rounded-lg mt-2 w-full", "placeholder": "ex : admin"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "rounded-lg mt-2 w-full"})
    )
    interface = forms.CharField(
        widget=forms.TextInput(attrs={"class": "rounded-lg mt-2 w-full", "placeholder": "ex : e1/0"}),
        label= 'interface'
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={"class": "rounded-lg mt-2 w-full", "placeholder": "ex : 192.x.x.x"}),
        label="Ip address"
    )
    mask = forms.CharField(
        widget=forms.TextInput(attrs={"class": "rounded-lg mt-2 w-full", "placeholder": "ex : 255.255.x.x"}),
        label="mask"
    )
    status = forms.CharField(
        widget=forms.TextInput(attrs={"class": "rounded-lg mt-2 w-full", "placeholder": "ex : no sh | sh"}),
        label="status",
        required=False
    )

class ConfigOspf(forms.Form):
    host = forms.CharField(
        widget=forms.TextInput(attrs={"class": "rounded-lg mt-2 w-full", "placeholder": "ex : 192.168.1.x"})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "rounded-lg mt-2 w-full", "placeholder": "ex : admin"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "rounded-lg mt-2 w-full"})
    )
    proccess_id = forms.CharField(
        widget=forms.TextInput(attrs={"class": "rounded-lg mt-2 w-full", "placeholder": "ex : 1"}),
        label= 'Process ID'
    )
    router_id = forms.CharField(
        widget=forms.TextInput(attrs={"class": "rounded-lg mt-2 w-full", "placeholder": "ex : 1.1.1.1"}),
        label="Router ID"
    )
    network = forms.CharField(

        required=True,

        widget=forms.widgets.Textarea(

            attrs={

                "placeholder": "ex :\n15.15.15.1\n12.12.12.1\n13.13.13.1",
                "class": "rounded-lg mt-3",
                "rows": 4

            }

        ),

        label="Network",
    )
    area = forms.CharField(

        required=True,

        widget=forms.widgets.Textarea(

            attrs={

                "placeholder": "ex :\n2\n2\n2",
                "class": "rounded-lg mt-3",
                "rows": 4
                

            }

        ),

        label="Area",
    )