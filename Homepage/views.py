from django.shortcuts import render
# Create your views here.

def HomePage1(request):
    return render(request, 'Homepage/homepage_1.html')


def HomePage2(request):
    return render(request, 'Homepage/homepage_2.html')