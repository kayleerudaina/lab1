from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create views.
def katalog_view (request):
    catalogitem = CatalogItem.objects.all()
    context = {
    'list_item': catalogitem,
    'nama': 'Kaylee Rudaina Danisha',
    'id': '2106654971'
    }
    return render(request, "katalog.html", context)