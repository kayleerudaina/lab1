from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create views.
def katalog_view (request):
    katalog_item = CatalogItem.objects.all()
    context = {
    'list_item': katalog_item,
    'Nama': 'Kaylee Rudaina Danisha',
    'ID': '2106654971'
    }
    return render(request, "katalog.html", context)