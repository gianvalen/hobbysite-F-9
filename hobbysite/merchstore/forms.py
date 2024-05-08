from django import forms

from .models import Product, Transaction


class MerchForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'stock_status': forms.Select(choices=Product.STATUS_CHOICES),
        }


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('amount', 'transaction_status')