from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'ITED/Home.html')


def gallery_page(request):
    return render(request, 'ITED/gallery.html')



def index_page(request):
    return render(request, 'ITED/index.html')




# def dashboard(request):
#     if not request.user.is_staff:
#         return redirect('/user/login')
#     context ={
#         'user_name': request.user.get_email()
#     }
#     return render(request, 'dashboard.html', context)


def contact_page(request):
    return render(request, 'ITED/contact.html')

def about_page(request):
    return render(request, 'ITED/aboutus.html')

def services1_page(request):
    return render(request, 'ITED/services1.html')

def services2_page(request):
    return render(request, 'ITED/services2.html')

def services3_page(request):
    return render(request, 'ITED/services3.html')



def services_page(request):
    return render(request, 'ITED/services.html')

def services4_page(request):
    return render(request, 'ITED/services4.html')

def services5_page(request):
    return render(request, 'ITED/services5.html')

def services6_page(request):
    return render(request, 'ITED/services6.html')

def services7_page(request):
    return render(request, 'ITED/services7.html')

def services8_page(request):
    return render(request, 'ITED/services8.html')

def services9_page(request):
    return render(request, 'ITED/services9.html')

def products1_page(request):
    return render(request, 'ITED/products1.html')


def products2_page(request):
    return render(request, 'ITED/products2.html')

def products3_page(request):
    return render(request, 'ITED/products3.html')

def disclaimer_page(request):
    return render(request, 'ITED/disclaimer.html')

def careers_page(request):
    return render(request, 'ITED/careers.html')

def test_page(request):
    return render(request, 'ITED/test.html')

def test1_page(request):
    return render(request, 'ITED/test1.html')
def index2_page(request):
    return render(request, 'ITED/index2.html')
def index3_page(request):
    return render(request, 'ITED/index3.html')
def pop_page(request):
    return render(request, 'ITED/pop.html')
def newpop_page(request):
    return render(request, 'ITED/newpop.html')


####################




