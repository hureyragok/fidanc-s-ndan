from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Settings, ContactFormMessage #,ContactFormu

from product.models import Product, Category

from home.forms import SearchForm, SignUpForm


def index(request):
    setting = Settings.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    dayproducts = Product.objects.all()[:4]
    lastproducts = Product.objects.all().order_by('-id')[:4]
    randomproducts = Product.objects.all().order_by('?')[:4]
    context = {'setting': setting,
               'category': category,
               'page': 'home',
               'sliderdata': sliderdata,
               'dayproducts': dayproducts,
               'lastproducts': lastproducts,
               'randomproducts': randomproducts}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category,}
    return render(request, 'hakkimizda.html', context)

def iletisim(request):

    """if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage() # model ile bağlantı kur
            data.name = form.cleaned_data['name'] # formdan bilgiyi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save() # veritabanına kaydet
            messages.success(request, "Mesajınız başarı ile gönderilmiştir. Teşekkür ederiz.")
            return HttpResponseRedirect('/iletisim')"""

    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    #form = ContactFormu()
    context = {'setting': setting, 'category': category}      #,'form': form}
    return render(request, 'iletisim.html', context)

def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    context = {'category': category, 'product': product}
    return render(request, 'product_detail.html', context)

def product_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=query)
            context = {'category': category, 'products': products}
            return render(request, 'products_search.html', context)

    return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Hatalı Kullanıcı Adı ya da Şifre!")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'login.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")

    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category, 'form': form}
    return render(request, 'signup.html', context)
