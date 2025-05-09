from django import forms

class CheckoutForm(forms.Form):
    firstName = forms.CharField(label="First name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastName = forms.CharField(label="Last name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    street = forms.CharField(label="Street Address", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.ChoiceField(label="Country / Region", choices=[('', 'Select'), ('Bangladesh', 'Bangladesh')], widget=forms.Select(attrs={'class': 'form-control'}))
    state = forms.ChoiceField(label="States", choices=[('', 'Select'), ('Dhaka', 'Dhaka'), ('Chittagong', 'Chittagong')], widget=forms.Select(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="Phone", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    notes = forms.CharField(label="Order Notes (Optional)", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notes about your order, e.g. special notes for delivery'}))
