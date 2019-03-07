from django.shortcuts import render
from django.http import HttpResponseForbidden, JsonResponse

# Create your views here.


def verify(request):
    """
    A testing URL for checking the API routes are working.

    @param {dict} request the django request object.
    """

    if request.method != 'GET':
        return HttpResponseForbidden()

    return JsonResponse({'msg': 'API V1 available'})
