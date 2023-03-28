from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from django.template.loader import get_template

from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.messages import constants

from django.contrib.auth.decorators import login_required

# PDF Create

from io import BytesIO

from xhtml2pdf import pisa

# Create your views here.

from .models import Laudo, LaudoMaterial
from .forms import LaudoForm, LaudoMaterialForm, LaudoMaterialFormset


@login_required(login_url='login')
def pageLaudos(request):
    laudos = Laudo.objects.all()
    context = {
        'laudos': laudos,
    }
    return render(request, 'laudos.html', context)


@login_required(login_url='login')
def insLaudo(request):
    if request.method == 'GET':
        form = LaudoForm()
        form_material_factory = inlineformset_factory(
            Laudo, LaudoMaterial, form=LaudoMaterialForm, extra=2)
        form_material = form_material_factory()
        context = {
            'form': form,
            'form_material': form_material,
        }
        return render(request, 'ins_laudo.html', context)
    elif request.method == 'POST':
        form = LaudoForm(request.POST)
        form_material_factory = inlineformset_factory(
            Laudo, LaudoMaterial, form=LaudoMaterialForm)
        form_material = form_material_factory(request.POST)
        if form.is_valid() and form_material.is_valid():
            laudo = form.save(commit=False)
            laudo.profissional = request.user
            laudo.save()
            form_material.instance = laudo
            form_material.save()
            messages.add_message(request, constants.SUCCESS,
                                 'Laudo salvo com sucesso!')
            return redirect(reverse('laudos'))
        else:
            context = {
                'form': form,
                'form_material': form_material,
            }
            messages.add_message(request, constants.ERROR,
                                 'Aconteceu um erro!')
            return redirect(reverse('ins_laudo'))


@login_required(login_url='login')
def upLaudo(request, id):
    laudo_instance = get_object_or_404(Laudo, id=id)
    if request.user.id == laudo_instance.profissional.id:
        template_name = 'up_laudo.html'
        form = LaudoForm(request.POST or None,
                         instance=laudo_instance, prefix='main')
        form_material = LaudoMaterialFormset(
            request.POST or None, instance=laudo_instance, prefix='items')

        if (
            request.method == 'POST'
            and form.is_valid()
            and form_material.is_valid()
        ):
            form.save()
            form_material.save()
            messages.add_message(request, constants.SUCCESS,
                                 'Laudo alterado com sucesso.')
            return redirect(reverse('up_laudo', kwargs={'id': id}))

        context = {
            'form': form,
            'form_material': form_material,
        }
        return render(request, template_name, context)
    else:
        messages.add_message(request, constants.WARNING,
                             'Você não tem permissão para alterar esse Laudo!')
        return redirect(reverse('laudos'))


@login_required(login_url='login')
def delItem(request, id):
    item = LaudoMaterial.objects.get(id=id)
    laudo = item.numero_laudo
    print(item.item.nome)
    item.delete()
    messages.add_message(request, constants.WARNING,
                         f'O item: {item.item.nome}. Foi removido com sucesso.')
    return redirect(reverse('up_laudo', kwargs={'id': laudo.id}))


def render_to_pdf(template_src, context_dict=None):
    if context_dict is None:
        context_dict = {}
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    return (
        None
        if pdf.err
        else HttpResponse(result.getvalue(), content_type='application/pdf')
    )


def gerar_pdf(request, id):
    laudo = Laudo.objects.get(id=id)
    context = {
        'laudo': laudo,
    }
    pdf = render_to_pdf('pdf_template.html', laudo)
    return HttpResponse(pdf, content_type='application/pdf')
