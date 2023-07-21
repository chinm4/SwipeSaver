from django.shortcuts import render
from commons.views import parse_html
from commons.views import remove_items
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'homepage.html')

def commons(request):
    remove_items(request)
    return parse_html(request)
    #return render(request, 'commons.html')

@csrf_exempt
def location(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_lat, user_lng = data['lat'], data['lng']

        # The location of the dining hall. Replace these with your actual coordinates
        dining_hall_lat, dining_hall_lng = 40.712776, -74.005974 

        # TODO: get API key for google maps
        api_key = 'YOUR_API_KEY' 

        url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={user_lat},{user_lng}&destinations={dining_hall_lat},{dining_hall_lng}&key={api_key}'

        response = requests.get(url).json()

        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Invalid Method'})