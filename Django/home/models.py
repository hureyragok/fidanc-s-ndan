from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.forms import TextInput, Textarea, ModelForm


class Settings(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    company = models.CharField(max_length=150)
    adress = models.CharField(blank=True, max_length=150)
    phone = models.CharField(max_length=150)
    fax = models.CharField(blank=True, max_length=150)
    email = models.CharField(blank=True, max_length=150)
    smtpserver = models.CharField(blank=True, max_length=150)
    smtpemail = models.CharField(blank=True, max_length=150)
    smtppassword = models.CharField(blank=True, max_length=150)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=150)
    instagram = models.CharField(blank=True, max_length=150)
    twitter = models.CharField(blank=True, max_length=150)
    about = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    status = models.CharField(choices=STATUS, max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
    )
    name = models.CharField(max_length=20)
    email = models.CharField(blank=True, max_length=150)
    subjects = models.CharField(blank=True, max_length=150)
    message = models.CharField(blank=True, max_length=250)
    status = models.CharField(choices=STATUS, max_length=10, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

"""class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Name&Surname'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'subject'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'message', 'rows': '5'}),
        }"""






