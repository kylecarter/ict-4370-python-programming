from django.http import HttpResponseForbidden, JsonResponse
from django.template import Context, Template
from django.views.generic import View

from bs4 import BeautifulSoup

from stocks.forms import StockByDateForm
# Create your views here.


def verify(request):
    """
    A testing URL for checking the API routes are working.

    @param {dict} request the django request object.
    """

    if request.method != 'GET':
        return HttpResponseForbidden()

    return JsonResponse({'msg': 'API V1 available'})


class GetForm(View):

    def get(self, request, form_name, * args, **kwargs):

        if form_name == 'stockbydate':
            form = StockByDateForm()
            t = Template('{{ form }}')
            c = Context({'form': form})
            soup = BeautifulSoup(t.render(c), 'html.parser')

            res = {}
            res['label'] = {
                'attributes': soup.label.attrs,
                'label': soup.label.string
            }
            res['input'] = {
                'attributes': soup.input.attrs
            }

            return JsonResponse({'form': res}, status=200)

        else:
            return JsonResponse({'msg': 'Form not found...'}, status=404)
