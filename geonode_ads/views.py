from django.shortcuts import render


def HomeScreen(request):
    return render(request, './templates/site_index.html')
