from django.shortcuts import render


def HomeScreen(request):
    return render(request, 'ads_site_index.html')
