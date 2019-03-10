from django.contrib import admin
from .models import Pet, Owner

# Register your models here.
class PetAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'birthdate']


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name']


admin.site.register(Pet, PetAdmin)
admin.site.register(Owner, OwnerAdmin)
