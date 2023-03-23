from django.shortcuts import render

# Create your views here.

def laudos(request):
    context = {}
    return render(request, 'laudos.html', context)