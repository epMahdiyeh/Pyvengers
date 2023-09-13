from django import forms

import django.core.validators as validators
from .models import Order, Pineapple, Seller, Comment


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'

    def clean_address(self):
        # apply model validation for address
        address = self.cleaned_data["address"]
        # add custom validation
        if len(address) < 10:
            raise forms.ValidationError("این فیلد باید بیشتر از ۱۰ کاراکتر باشد.")
        return address

    def clean_certificate_code(self):
        # apply model validation for certificate_code
        clean_certificate = self.cleaned_data["certificate_code"]
        # add custom validation
        if not clean_certificate.isupper():
            raise forms.ValidationError("حروف گواهینامه باید حروف بزرگ باشد.")
        return clean_certificate


class PineappleForm:
    pass


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean_weight_kg(self):
        weight_kg = self.cleaned_data["weight_kg"]
        if weight_kg > 100:
            raise forms.ValidationError('۱۰۰ کیلو آناناس میخوای چیکار؟ مشکل داری؟')
        return weight_kg


class SubscriptionForm:
    pass


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
