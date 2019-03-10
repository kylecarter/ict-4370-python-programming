from django.db import models
import datetime

# Create your models here.
class Pet(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, verbose_name="Pet Owner")
    type_of_pet = models.CharField(max_length=255, verbose_name=u"Type of pet")
    birthdate = models.DateField(verbose_name="Date")
    name = models.CharField(max_length=255, verbose_name=u"Name")
    breed = models.CharField(max_length=255, verbose_name=u"Breed", null=True)
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Weight in Kilograms")


    def get_age(self):
        return datetime.date.today().year - self.birthdate.year


class Owner(models.Model):
    first_name = models.CharField(max_length=255, verbose_name=u"First Name")
    last_name = models.CharField(max_length=255, verbose_name=u"Last Name")


    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
