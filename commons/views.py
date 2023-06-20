from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def scrape_website(request):
    url = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15465&locationId=76929001&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Scrape the data you need from the BeautifulSoup object
    # Store the extracted data in variables or a context dictionary
    # Pass the data to the template or return a JSON response
    return render(request, 'scraped_data.html', {'data': extracted_data})

def home(request):
    return HttpResponse("Welcome to SwipeSaver!")

def commons(request):
    return HttpResponse("Welcome to Commons!")