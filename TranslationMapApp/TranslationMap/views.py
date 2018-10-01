# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json
import requests
from .forms import getWord

# Create your views here.
def index(request):

    context = {}
    countries = {
        'Iceland' : 'is',
        'Spain' : 'es',
        'Germany' : 'de',
        'France' : 'fr',
        'Ireland' : 'ga',
        'England' : 'en',
        'Scotland' : 'gd',
        'Wales' : 'cy',
        'Netherlands' : 'nl',
        'Spain' : 'es',
        'Portugal' : 'pt',
        'Denmark' : 'da',
        'Norway' : 'no',
        'Sweden' : 'sv',
        'Finland' : 'fi',
        'Estonia' : 'et',
        'Latvia' : 'lv',
        'Lithuania' : 'lt',
        'Luxembourg' : 'lb',
        'Russia' : 'ru',
        'Belarus' : 'be',
        'Ukraine' : 'uk',
        'Poland' : 'pl',
        'Czechia' : 'cs',
        'Slovakia' : 'sk',
        'Slovenia' : 'sl',
        'Romania' : 'ro',
        'Bulgaria' : 'bg',
        'Serbia' : 'sr',
        'Hungary' : 'hu',
        'Croatia' : 'hr',
        'Greece' : 'el',
        'Georgia' : 'ka',
        'Italy' : 'it',
        'Turkey' : 'tr',
    }

    form = getWordForm()
    word = post(request)

    if word != '':
        for country, code in countries.items():
            translation = getTranslation(code, word)
            context[country] = translation

    context["form"] = form

    return render(request, 'TranslationMap/index.html', context)

def getWordForm():
    form = getWord()
    return form

def post(request):
    form = getWord(request.POST)
    text = ''
    if form.is_valid():
        text = form.cleaned_data['word']
    return text

def getTranslation(language, word):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20180527T143501Z.a7a28c5351395283.7f23654a4c75fec66cba97a8d0f8be8008c1cee1&text=' + word + '&lang=' + language + '&[format=utf-8'
    response = requests.get(url)
    data = json.loads(response.content.decode('utf-8'))
    translation = ''.join(data['text'])
    return translation