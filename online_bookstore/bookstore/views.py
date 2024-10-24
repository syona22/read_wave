from django.shortcuts import render
from .models import Book

def home(request):
    best_sellers = Book.objects.filter(is_best_seller=True)

    return render(request, 'homepage.html', {
        'best_sellers': best_sellers,
    })

def trending(request):
    return render(request, 'trending.html')

def fiction(request):
    return render(request, 'fiction.html')

def animation(request):
    return render(request, 'animationpage.html')

def adventure(request):
    return render(request, 'adventurepage.html')

def biography(request):
    return render(request, 'biography.html')

def payment(request):
    return render(request, 'payment.html')

def otp(request):
    return render(request, 'otp_verification.html')

def about(request):
    return render(request,'about us.html')

def harry(request):
    return render(request,'Harry.html')

def pay_harry(request):
    return render(request,'payharry.html')

def otp_harry(request):
    return render(request,'otp_harry.html')

def thankharry(request):
    return render(request,'thankharry.html')

def trending(request):
    return render(request,'trending.html')

def davin(request):
    return render(request,'Da Vinci.html')

def pay_da(request):
    return render(request,'payda.html')

def otp_da(request):
    return render(request,'otp_verification.html')

def thankda(request):
    return render(request,'thankda.html')

def blog(request):
    return render(request,'blog.html')
    