from django.views.generic import View
from django.http import JsonResponse

from .models import Stock, Symbol

# Create your views here.
class Symbols(View):
    model = Symbol

    def get(self, request, *args, **kwargs):
        symbols = Symbol.objects.all()
        companies = []

        for symbol in symbols:
            companies.append({
                'symbol': symbol.symbol,
                'business': symbol.business,
                'id': symbol.id
            })

        return JsonResponse({'symbols': companies})


class StockDetails(View):
    model = Stock

    def get(self, request, symbol_id, * args, **kwargs):
        stocks = Stock.objects.filter(symbol__id=symbol_id).order_by('date')
        details = []

        for stock in stocks:
            details.append({
                'symbol': stock.symbol.symbol,
                'id': stock.id,
                'open': stock.open_price,
                'close': stock.close_price,
                'high': stock.high_price,
                'low': stock.low_price,
                'volume': stock.volume,
                'date': stock.date
            })

        return JsonResponse({
            'stocks': details,
            'symbol': stocks[0].symbol.symbol.upper(),
            'business': stocks[0].symbol.business.title()
        })
