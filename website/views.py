from django.shortcuts import render

# Create your views here.
def about(request):
    context = {
        "title":"About Us"
    }    
    return render(request, 'website/about.html', context=context)

def index(request):
    return render(request, "website/index.html")

def contact(request):
    context = {
        "title":"Contact Us"
    }
    return render(request, "website/contact.html", context=context)

def av(request):
    context = {
        "title":"AV  Equipment Rental"
    }
    return render(request, "website/av_equipment.html", context=context)
def audio(request):
    context = {
        "title":"Audio"
    }
    return render(request, "website/av_equipment.html", context=context)

def lighting(request):
    context = {
        "title":"Lighting"
    }
    return render(request, "website/av_equipment.html", context=context)
def backline(request):
    context = {
        "title":"backline"
    }
    return render(request, "website/av_equipment.html", context=context)
def staging(request):
    context = {
        "title":"Staging"
    }
    return render(request, "website/av_equipment.html", context=context)
def special(request):
    context = {
        "title":"Special Efects"
    }
    return render(request, "website/av_equipment.html", context=context)
def work(request):
    context = {
        "title":"Featured Work"
    }
    return render(request, "website/av_equipment.html", context=context)
def careers(request):
    context = {
        "title": "We are Hiring"
    }
    return render(request, "website/av_equipment.html", context=context)    