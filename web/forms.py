from django import forms


class ConfigForm(forms.Form):
    show_password = forms.BooleanField(label="Show Passwords", required=False)
    save_password = forms.BooleanField(label="Save Passwords", required=False)
    # TODO insert wifi networks
    network = forms.ChoiceField(choices=[("1", 1), ("2", 2)], widget=forms.Select(), required=True, label="Network")

