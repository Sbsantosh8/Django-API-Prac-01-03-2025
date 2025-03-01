from django.shortcuts import render


def home(request):
    greet = "hello"
    return render(request, "index.html", {"greet": greet})
