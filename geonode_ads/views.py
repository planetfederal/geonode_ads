from django.shortcuts import render
from django.conf import settings


def HomeScreen(request):
    if hasattr(settings, 'SITENAME'):
        if settings.SITENAME == 'exchange':
            return render(request, 'ads_exchange_index.html')
    else:
        return render(request, 'ads_geonode_index.html')
