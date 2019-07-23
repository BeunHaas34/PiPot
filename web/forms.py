from django import forms
from web.networks import getNetworks

class ConfigForm(forms.Form):
    networks = getNetworks()
    network = forms.ChoiceField(choices=networks, widget=forms.Select(), required=True, label="Network")

