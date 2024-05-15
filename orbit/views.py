from django.shortcuts import render, redirect
from .models import About, Portfolio, Category, Server, Resume, Cleant
from .forms import ContactForm


# Create your views here.


def index(request):
    about = About.objects.all()
    porfolio = Portfolio.objects.all()
    category = Category.objects.all()
    server = Server.objects.all()
    resume = Resume.objects.all()
    cleant = Cleant.objects.all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    ctx = {
        "about": about,
        "portfolio": porfolio,
        "category": category,
        "server": server,
        "resume": resume,
        "cleant": cleant,
        'form': form
    }
    return render(request, 'index.html', ctx)


from django.shortcuts import render

# Create your views here.
