from django.http import HttpResponse

def homepage(request):
    return HttpResponse("this is our homepage")

def contact(request):
    return HttpResponse("contact page")

def product(request):
    return HttpResponse("product page")