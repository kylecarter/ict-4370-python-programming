from django.views.generic import View
from django.http import JsonResponse

from .models import Pet, Owner


# Create your views here.
class Companions(View):
    model = Pet

    def get(self, request, *args, **kwargs):
        pets = Pet.objects.all()
        companions = []

        for pet in pets:
            companions.append({
                'id': pet.id,
                'name': pet.name,
                'type': pet.type_of_pet,
                'breed': pet.breed,
                'age': pet.get_age(),
                'birthdate': pet.birthdate,
                'weight': pet.weight,
                'owner': pet.owner.get_full_name()
            })

        return JsonResponse({'companions': companions})
