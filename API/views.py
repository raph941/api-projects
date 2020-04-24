from django.shortcuts import render
from ggcode.models import GeoCode

def home(request):
    obj = GeoCode.objects.get(pk=1)
    r_requests = obj.request_count

    context = {
        'r_requests': r_requests
    }

    return render(request, 'home.html', context)