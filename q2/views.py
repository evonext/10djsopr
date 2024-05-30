import math
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def resist_calculator(request):
    r1 = ""
    r2 = ""
    r = ""

    if request.method == "POST":
        r1 = request.POST.get("r1")
        r2 = request.POST.get("r2")
        button = request.POST.get("button")

        if button == "Очистить":
            r1 = ""
            r2 = ""

        elif button == "Вычислить" and len(r1) > 0 and len(r2) > 0:
            r = round(1 / (1 / int(r1) + 1 / int(r2)), 2)

    context = {"r1": r1, "r2": r2, "r": r}
    return render(request, "resist_calculator.html", context)
