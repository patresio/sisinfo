from django.shortcuts import render

from django.contrib.auth.decorators import login_required
# Create your views here.

from laudos.models import Laudo
from equipamentos.models import Equipamento


@login_required(login_url='login')
def dashboard(request):
    laudos_user = Laudo.objects.filter(profissional=request.user)
    laudos = Laudo.objects.all()

    equipamentos = Equipamento.objects.all()

    total_laudos = laudos.count()
    laudos_abertos = laudos.filter(status='01').count()
    total_laudos_user = laudos_user.count()
    total_laudos_user_abertos = laudos_user.filter(status='01').count()

    total_equipamentos = equipamentos.count()
    total_equipamentos_ativos = equipamentos.filter(status='1').count()

    context = {
        'total_laudos': total_laudos,
        'laudos_abertos': laudos_abertos,
        'total_laudos_user': total_laudos_user,
        'total_laudos_user_abertos': total_laudos_user_abertos,
        'total_equipamentos': total_equipamentos,
        'total_equipamentos_ativos': total_equipamentos_ativos,
    }
    return render(request, 'index.html', context)
