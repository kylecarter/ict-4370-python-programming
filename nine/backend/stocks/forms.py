from django import forms

from .models import Stock

class StockByDateForm(forms.Form):
    error_css_class = 'is-invalid'
    required_css_class = 'required'

    min_date_stock = Stock.objects.earliest('date')
    max_date_stock = Stock.objects.latest('date')

    date = forms.DateField(required=True, label='Enter a Date', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'required': 'required',
        'min': min_date_stock.date.strftime('%Y-%m-%d'),
        'max': max_date_stock.date.strftime('%Y-%m-%d')
    }))
