from django.contrib import admin
from .models import ContactForm,QuoteForm

# Register your models here.
admin.site.register(ContactForm)
admin.site.register(QuoteForm)