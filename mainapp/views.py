from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionsForm, ReviewForm, OtinishVakForm, RequestHelpForm
from .models import *


def index(request):
    reviews = Reviews.objects.order_by('-publish')[:3]
    context = {'title': 'Басты бет', 'reviews': reviews}
    return render(request, 'mainapp/index.html', context)


def about(request):
    context = {'title': 'Біз туралы', }
    return render(request, 'mainapp/about-us.html', context)


def news(request):
    news = News.objects.order_by('-created_at')
    context = {'title': 'Жаңалықтар', 'news': news}
    return render(request, 'mainapp/news.html', context)


def search_homes(request):
    homes = Home.objects.all()
    context = {'title': 'Тұрғын үй іздеу', 'homes': homes}
    return render(request, 'mainapp/homes.html', context)


def detailnews(request, slug):
    question = get_object_or_404(News, slug=slug)
    context = {'new': question}
    return render(request, 'mainapp/news-details.html', context)


def detailhomes(request, slug):
    question = get_object_or_404(Home, slug=slug)
    context = {'home': question}
    return render(request, 'mainapp/homes-details.html', context)


def free_lands(request):
    context = {'title': 'ЖАО сайттарында шаруашылыққа бос жер туралы ақпарат'}
    return render(request, 'mainapp/free_lands.html', context)


def data(request):
    datas = Data.objects.all()
    context = {'title': 'Мәліметтер', 'datas': datas}
    return render(request, 'mainapp/data.html', context)


def vakancia(request):
    vakancia = Vakancia.objects.all()
    context = {'title': 'Мәліметтер', 'vakancia': vakancia}
    return render(request, 'mainapp/vakancia.html', context)


def vakanciaotinish(request):
    if request.method == 'POST':
        form = OtinishVakForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('home')
    form = OtinishVakForm()
    context = {
        'form': form,
        'title': 'Өтініш беру'
    }
    return render(request, 'mainapp/clientotinish.html', context)


def clienthelp(request):
    if request.method == 'POST':
        form = RequestHelpForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('home')
    form = RequestHelpForm()
    context = {
        'form': form,
        'title': 'Өтініш беру'
    }
    return render(request, 'mainapp/clienthelp.html', context)


def azamattyq(request):
    context = {'title': 'Азаматтық алу'}
    return render(request, 'mainapp/info_azamattyq.html', context)


def zher(request):
    jer = Jer.objects.all()
    context = {'title': 'Жер учаскесі', 'jer': jer}
    return render(request, 'mainapp/info_zher.html', context)


def help(request):
    context = {'title': 'Әлеуметтік көмек'}
    return render(request, 'mainapp/info_help.html', context)


def homerequest(request):
    otinishvak = OtinishVak.objects.order_by('-publish')
    reviews = Reviews.objects.order_by('-publish')
    requests = RequestHelp.objects.order_by('-publish')
    questions = Questions.objects.order_by('-publish')
    context = {'title': 'Өтініштер', 'otinishvak': otinishvak, 'requests': requests,
               'reviews': reviews, 'questions': questions}
    return render(request, 'mainapp/homerequest.html', context)


def contact(request):
    form = ReviewForm()
    context = {'title': 'Контактілер', 'form': form}

    return render(request, 'mainapp/contact.html', context)


def addreview(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('home')


def questions(request):
    form = QuestionsForm()
    context = {'title': 'Сұрағыңызды қойыңыз', 'form': form}

    return render(request, 'mainapp/raise_question.html', context)


def addquestion(request):
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('home')
