from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactForm,QuoteForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        data = {}
        for key in request.POST:
            if key == "csrfmiddlewaretoken" or key == 'name':
                pass
            else:
                data[key] = request.POST.get(key)
        form = QuoteForm(**data)
        form.save()
        return HttpResponse(f"Form Submitted {data}")
    else:
        context = {
            "title": "JF Sounds",
            "is_contact": True

        }
        return render(request, "website/index.html", context=context)
    
def about(request):
    context = {
        "title":"About Us"
    }    
    return render(request, 'website/about.html', context=context)


def contact(request):
    if request.method == 'POST':
        data = {}
        for key in request.POST:
            if key == "csrfmiddlewaretoken":
                pass
            else:
                data[key] = request.POST.get(key)
        form = ContactForm(**data)
        form.save()
        return HttpResponse(f"Form Submitted {data}")
    else:
        context = {
            "title": "Contact Us",
            "is_contact": True
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
        "title":"Backline"
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
        "title": "We are Hiring",
        "is_contact": True

    }
    return render(request, "website/av_equipment.html", context=context)    