from django import forms


class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_name = forms.CharField()
    requiers_name = forms.ChoiceField()
    dekivery_name = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField()