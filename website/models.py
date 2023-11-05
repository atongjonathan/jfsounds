from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    number = models.IntegerField(blank=True)
    info = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

class QuoteForm(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    number = models.IntegerField(blank=True)
    state = models.CharField(max_length=100, blank=True)
    budget = models.CharField(max_length=100, blank=True)
    date = models.DateField(blank=True)
    info = models.CharField(max_length=100, blank=True)
    audio = models.CharField(max_length=100, blank=True)
    video = models.CharField(max_length=100, blank=True)
    staging = models.CharField(max_length=100, blank=True)
    special = models.CharField(max_length=100, blank=True)
    lighting = models.CharField(max_length=100, blank=True)
    backline = models.CharField(max_length=100, blank=True)
    crowd = models.CharField(max_length=100, blank=True)


    def __str__(self) -> str:
        return f"{self.first_name}'s Quotation Request"

