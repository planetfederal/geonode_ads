from django.shortcuts import render
from django.conf import settings


def HomeScreen(request):
    if hasattr(settings, 'SITE_NAME'):
        if settings.SITE_NAME == 'exchange':
            return render(request, 'ads_exchange_index.html')
    else:
        return render(request, 'ads_geonode_index.html')
