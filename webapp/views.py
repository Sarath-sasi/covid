from django.shortcuts import render
from .models import FormClass
from .models import csClass

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    d = {
        'head': 'Treatment',
        'dec': 'Sed in metus libero. Sed volutpat eget dui ut tempus. Fusce fringilla tincidunt laoreet',

    }
    return render(request, 'services.html', d)


def contact(request):
    if request.method=='POST':
        yname = request.POST['Name']
        yemail = request.POST['Email']
        subj = request.POST['Subject']
        mg = request.POST['Message']
        csClass.objects.create(name=yname, eml=yemail, sbt=subj, mess=mg)
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')

def register(request):
    if request.method=='POST':
        em = request.POST['email']
        passw = request.POST['psw']
        cfpass = request.POST['psw-repeat']
        FormClass.objects.create(name=em, age=passw, text=cfpass)
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def search(request):
    data = request.GET['search']
    objects = csClass.objects.filter(name=data)
    return render(request, 'search.html', {'obj': objects})
# Create your views here.
