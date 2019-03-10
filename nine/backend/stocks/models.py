from django.db import models

# Create your models here.
class Stock(models.Model):
    symbol = models.ForeignKey(
        'Symbol', on_delete=models.CASCADE, verbose_name="Stock Symbol")
    open_price = models.DecimalField(
        max_digits=15, decimal_places=2, verbose_name="Open")
    close_price = models.DecimalField(
        max_digits=15, decimal_places=2, verbose_name="Close")
    high_price = models.DecimalField(
        max_digits=15, decimal_places=2, verbose_name="High")
    low_price = models.DecimalField(
        max_digits=15, decimal_places=2, verbose_name="Low")
    volume = models.IntegerField(verbose_name="Volume")
    date = models.DateField(verbose_name="Date")


class Symbol(models.Model):
    symbol = models.CharField(max_length=255, verbose_name=u"Stock Symbol")
    business = models.CharField(max_length=255, verbose_name=u"Business Name")
