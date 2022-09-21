from django.urls import path
from mywatchlist.views import watchlist_view
from mywatchlist.views import show_json
from mywatchlist.views import show_xml

# TODO: Implement Routings Here
app_name = 'mywatchlist'

urlpatterns = [
    path('', watchlist_view, name = 'watchlist_view'),
    path('html/', watchlist_view, name='watchlist_view'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]