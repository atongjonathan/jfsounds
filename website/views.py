from django.shortcuts import render
from .models import ContactForm,QuoteForm
import smtplib
import os

password = os.getenv("APP_PASSWORD")
def send_email(sender, reciever, content):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()  # Secure connection
        connection.login(user=sender, password=password)
        try:
            connection.sendmail(from_addr=sender,
                                to_addrs=reciever,
                                msg=f"Subject:Quotation\n\n{content}")
            print("Sent")
        except UnicodeError:
            print("Not Sent")
def index(request):
    context = {
        "title": "JF Sounds",
        "is_contact": True
    }
    if request.method == 'POST':
        data = {}
        for key in request.POST:
            if key == "csrfmiddlewaretoken":
                pass
            else:
                data[key] = request.POST.get(key)
        form = QuoteForm(**data)
        form.save()
        context["is_success"] = True
        content = '\n'.join([f"{key.title()}: {value}" for key,value in data.items()])
        send_email("atongjonathan@gmail.com",data["email"], content)
    return render(request, "website/index.html", context=context)
    
def about(request):
    context = {
        "title":"About Us",
        "is_contact": True

    }    
    return render(request, 'website/about.html', context=context)


def contact(request):
    context = {
        "title": "Contact Us",
        "is_contact": True
    }
    if request.method == 'POST':
        data = {}
        for key in request.POST:
            if key == "csrfmiddlewaretoken":
                pass
            else:
                data[key] = request.POST.get(key)
        form = ContactForm(**data)
        form.save()
        context["is_success"] = True
        # return HttpResponseRedirect(reverse("contact"))
    return render(request, "website/contact.html", context=context)

def av(request):
    context = {
        "title":"AV  Equipment Rental"
    }
    return render(request, "website/av_equipment.html", context=context)
def success(request):
    context = {
        "title":"Success"
    }
    return render(request, "website/success.html", context=context)
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
        "title":"Special Effects"
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