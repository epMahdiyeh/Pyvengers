from django import forms
from .models import Comment

class SellerForm:
    pass

class PineappleForm:
    pass

class OrderForm:
    pass

class SubscriptionForm:
    pass

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
