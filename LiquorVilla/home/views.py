from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    # return HttpResponse("Home Page")
    sendVariable = {
        "value1":4
    }
    
    return render(request,  "index.html", sendVariable)


def about(request):
    # return HttpResponse("About Page, \nWe have something for everyone.")
    return render(request,  "about.html")

def services(request):
    # return HttpResponse("Services Page")
    return render(request,  "services.html") 


def contact(request):
    # return HttpResponse("Contacts Page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email=email, desc=desc, date=datetime.today())
        contact.save()
    return render(request,  "contact.html")
