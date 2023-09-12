from django import forms
from django.core.validators import MaxValueValidator
from .models import Order, Pineapple


class SellerForm:
    pass


class PineappleForm:
    pass


class OrderForm(forms.ModelForm):
    pineapple = forms.ModelChoiceField(queryset=Pineapple.objects.all())

    class Meta:
        model = Order
        fields = '__all__'

    name = forms.CharField(max_length=50)
    weight_kg = forms.FloatField(validators=[
        MaxValueValidator(100, '۱۰۰ کیلو آناناس میخوای چیکار؟ مشکل داری؟')
    ])


class SubscriptionForm:
    pass


class CommentForm:
    pass
