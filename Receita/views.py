from django.shortcuts import render


def home(request):
    return render(request, "Receita/page/home.html")
