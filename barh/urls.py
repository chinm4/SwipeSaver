from django.urls import path
from . import views

urlpatterns = [

    path('parse-html/', views.parse_html, name='parse_html'),
    path('remove_items', views.remove_items, name='remove_items'),
    path('', views.barh, name='barh'),
    path('rate/', views.rate, name='rate'),

]
