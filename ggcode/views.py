from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from .models import GeoCode
from .utils import GetNearCities


def GeoCodeView(request):
    if request.method == 'POST':
        address = request.POST['address']
        url = "https://google-maps-geocoding.p.rapidapi.com/geocode/json"
        querystring = {"language":"en","address":address}
        headers = {
            'x-rapidapi-host': "google-maps-geocoding.p.rapidapi.com",
            'x-rapidapi-key': "8840d3da12msh74280e203685253p142c1djsnee61630c4777"
            }
        response = requests.request("GET", url, headers=headers, params=querystring) #api call
        free_requests_count = response.headers.get('X-RateLimit-Requests-Remaining') 
        if not GeoCode.objects.get(pk=1):
            GeoCode.objects.create(request_count=0)
        obj = GeoCode.objects.get(pk=1)
        obj.request_count = free_requests_count
        obj.save()
        response = response.json()

        if response.get('status') == 'OK':
            f_address = response.get('results')[0].get('formatted_address')
            input_address = response.get('results')[0].get('address_components')[0].get('long_name')
            lat = response.get('results')[0].get('geometry').get('location').get('lat')
            lng = response.get('results')[0].get('geometry').get('location').get('lng')
            near_cities = GetNearCities(lat, lng)

            data = {
                "f_address": f_address,
                'input_address': input_address,
                'lat': lat,
                'lng': lng,
                'free_request': free_requests_count,
                'near_cities': near_cities
            }
        else:
            data = {
                "response": 'there is no result for your query'
            }
        # import pdb; pdb.set_trace()
        # me=34

        return JsonResponse(data)

