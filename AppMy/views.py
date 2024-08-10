from django.shortcuts import render

# Create your views here.

def indexPage(request):
    context = {}

    return render(request,"index.html",context)


def frcPage(request):
    context = {}

    return render(request,"frc.html",context)

def sponsorlarPage(request):
    context = {}

    return render(request,"sponsorlarimiz.html",context)

def haberlerPage(request):
    context = {}

    return render(request,"haberler.html",context)

def iletisimPage(request):
    context = {}

    return render(request,"iletisim.html",context)