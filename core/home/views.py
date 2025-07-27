from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    data = [
        {"name": "Ali", "age": 25, "city": "Lahore"},
        {"name": "Sara", "age": 30, "city": "Karachi"},
        {"name": "Ahmed", "age": 28, "city": "Islamabad"},
    ]
    text = 'Ali said, "Hello there!"'
    return render(request, 'home.html', {"data": data, "text": text})
def contact(request):
    return render(request, 'contact.html', {"text": "Contact us at Ali's email."})
def about(request):
    return render(request, 'about.html', {"text": "About us page content."})
def hi(request):
    return HttpResponse("Hello, How are you doing?")
