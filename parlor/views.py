from django.shortcuts import render,HttpResponse
from datetime import datetime
from parlor.models import Contact
from django.contrib import messages
from .models import Icecreame

# Create your views here.
def index(request):

    ice1 = Icecreame()
    ice1.img = '1.jpg'
    ice1.desc = 'Chocolate Crumb Cheesecake – cheesecake ice cream with chocolate cookie swirl.'
    ice1.id = '1'
    ice1.price = '$3'
    ice1.name = 'Chocolate Crumb Cheesecake'

    ice2 = Icecreame()
    ice2.img = '2.jpg'
    ice2.desc = 'Oreo® Cookie – Vanilla ice cream with crushed Oreo® cookies.'
    ice2.id = '2'
    ice2.price = '$5'
    ice2.name = 'Oreo® Cookie'

    ice3 = Icecreame()
    ice3.img = '3.jfif.jpg'
    ice3.desc = 'Strawberry Cheese Icecreame– Cheesex ice cream with strawberry swirl.'
    ice3.id = '3'
    ice3.price = '$2'
    ice3.name = 'Strawberry Cheese Icecreame'

    ice4 = Icecreame()
    ice4.img = '4.jfif.jpg'
    ice4.desc = 'Cake Batter – Cake batter ice cream with cupcake bites.'
    ice4.id = '4'
    ice4.price = '$5'
    ice4.name = 'Cake Batter'

    ice5 = Icecreame()
    ice5.img = '5.jfif.jpg'
    ice5.desc = 'Coffee – Simply stated; creamy smooth classic coffee.'
    ice5.id = '5'
    ice5.price = '$4'
    ice5.name = 'Coffee'

    ice6 = Icecreame()
    ice6.img = '6.jfif.jpg'
    ice6.desc = 'Vanilla – Simply stated; creamy classic vanilla.'
    ice6.id = '6'
    ice6.price = '$3'
    ice6.name = 'Vanilla'

    ice7 = Icecreame()
    ice7.img = '7.jfif.jpg'
    ice7.desc = 'French Vanilla – A classic vanilla ice cream blended with smooth egg custard.'
    ice7.id = '7'
    ice7.price = '$2'
    ice7.name = 'French Vanilla'

    ice8 = Icecreame()
    ice8.img = '8.jfif.jpg'
    ice8.desc = 'Lemon Meringue Pie – Creamy & light lemon chiffon ice cream cracker swirl.'
    ice8.id = '8'
    ice8.price = '$4'
    ice8.name = 'Lemon Meringue Pie'

    ice9 = Icecreame()
    ice9.img = '9.jfif.jpg'
    ice9.desc = 'Chocolate – Traditional rich New England chocolate.'
    ice9.id = '9'
    ice9.price = '$3'
    ice9.name = 'Chocolate'

    ices = [ice1, ice2, ice3, ice4, ice5, ice6, ice7, ice8, ice9]
    return render(request, 'index.html',{'ices':ices})
    # return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'Services.html')
    #return HttpResponse("this is services page")

def chocolate(request):
    return render(request, 'chocolate.html')

def butterscotch(request):
    return render(request, 'butterscotch.html')


def familypack(request):
    return render(request, 'familypack.html')


def contact(request): 
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name,email = email ,phone = phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, 'your details sent.')
    return render(request, 'contact.html')
    #return HttpResponse("this is contact page")

    
def to_str(value):
    return str(value)

