from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('contact/', contact, name='contact'),
    path('azamattyq/', azamattyq, name='azamattyq'),
    path('info_zher/', zher, name='info_zher'),
    path('info_help/', help, name='info_help'),
    path('info_help/help', clienthelp, name='clienthelp'),
    path('about-us/', about, name='about'),
    path('news/', news, name='news'),
    path('data/', data, name='data'),
    path('request/', homerequest, name='homerequest'),
    path('vakancia/', vakancia, name='vakancia'),
    path('vakancia/otinish', vakanciaotinish, name='vakanciaotinish'),
    path('search_homes/', search_homes, name='search_homes'),
    path('news/<slug:slug>/', detailnews, name='detailnews'),
    path('search_homes/<slug:slug>/', detailhomes, name='detailhomes'),
    path('free_lands/', free_lands, name='free_lands'),
    path("addreview/", addreview, name="addreview"),
    path("question/", questions, name="question"),
    path("addquestion/", addquestion, name="addquestion"),
    path('contact/', contact, name='contact'),
]
