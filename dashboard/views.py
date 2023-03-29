from django.shortcuts import render

from django.contrib.auth.decorators import login_required
# Create your views here.

from laudos.models import Laudo


@login_required(login_url='login')
def dashboard(request):
    laudos = Laudo.objects.all()

    total_laudos = laudos.count()
    laudos_abertos = laudos.filter(status='01').count()
    context = {
        'total_laudos': total_laudos,
        'laudos_abertos': laudos_abertos,
    }
    return render(request, 'index.html', context)
