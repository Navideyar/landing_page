from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # صفحه اصلی را نمایش بده

def single_page(request):
    return render(request, 'single.html')  # صفحه دوم را نمایش بده