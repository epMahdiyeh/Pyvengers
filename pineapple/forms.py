import re
from django import forms
from .models import Subscription, Order, Pineapple, Seller, Comment


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'

    def clean_address(self):
        # apply model validation for address
        address = self.cleaned_data.get("address")
        # add custom validation
        if len(address) < 10:
            raise forms.ValidationError("این فیلد باید بیشتر از ۱۰ کاراکتر باشد.")
        return address

    def clean_certificate_code(self):
        # apply model validation for certificate_code
        clean_certificate = self.cleaned_data.get("certificate_code")
        # add custom validation
        if not clean_certificate.isupper():
            raise forms.ValidationError("حروف گواهینامه باید حروف بزرگ باشد.")
        return clean_certificate


class PineappleForm(forms.ModelForm):
    class Meta:
        model = Pineapple
        fields = '__all__'

    def clean_price_toman(self):
        price_toman = self.cleaned_data.get('price_toman')
        if price_toman < 1000:
            raise forms.ValidationError("قیمت نباید کمتر از هزار تومان باشد.")
        elif price_toman > 1000000:
            raise forms.ValidationError("قیمت نباید از یک میلیون تومان بیشتر باشد.")
        return price_toman


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean_weight_kg(self):
        weight_kg = self.cleaned_data.get("weight_kg")
        if weight_kg > 100:
            raise forms.ValidationError('۱۰۰ کیلو آناناس میخوای چیکار؟ مشکل داری؟')
        return weight_kg


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = '__all__'

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        pattern = re.compile(r'^09\d{9}$')
        if not pattern.match(phone_number):
            raise forms.ValidationError('شماره تلفن اشتباه است. شماره تلفن باید ۱۱ رقم باشد و با ۰۹ شروع شود.')
        return phone_number


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        

    def clean_text(self):
        content = self.cleaned_data.get('text')
        if len(content) < 10:
            raise forms.ValidationError("این فیلد باید بیشتر از ۱۰ کاراکتر باشد.")
        return content
    