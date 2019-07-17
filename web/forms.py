from django import forms
from web.networks import getNetworks

class ConfigForm(forms.Form):
    show_password = forms.BooleanField(label="Show Passwords", required=False)
    save_password = forms.BooleanField(label="Save Passwords", required=False)

    networks = getNetworks()
    network = forms.ChoiceField(choices=networks, widget=forms.Select(), required=True, label="Network")

