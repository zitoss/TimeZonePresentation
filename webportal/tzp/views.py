from django.shortcuts import render

# Create your views here.


def single_view(request):
    u""" View for representing single timezone information """
    return render(request, 'single.html')
