from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants

from PIL import Image, ImageDraw
from datetime import date
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your views here.

from .models import Equipamento, Imagem
from setores.models import Setor


def equipamentos(request):
    equipamentos = Equipamento.objects.all()
    context = {
        'equipamentos': equipamentos,
    }
    return render(request, 'equipamentos.html', context)


def viewEquipamento(request, id):
    equipamento = Equipamento.objects.get(id=id)
    imagens = Imagem.objects.filter(equipamento=Equipamento(id=id))
    context = {
        'equipamento': equipamento,
        'imagens': imagens,
    }
    return render(request, 'view_equipamento.html', context)


def addEquipamentos(request):
    if request.method == "GET":
        status_choices = Equipamento.status_choices
        tipo_choices = Equipamento.tipo_choices
        setores = Setor.objects.all()
        context = {
            'status': status_choices,
            'tipo': tipo_choices,
            'setores': setores,
        }
        return render(request, 'add_equipamento.html', context)
    elif request.method == "POST":
        return extrair_forms_equipamento(request)


def delEquipamento(request, id):
    equipamento = Equipamento.objects.get(id=id)
    imagens = Imagem.objects.filter(equipamento=id)
    # Remove as imagens primeiro
    for imagem in imagens:
        imagem.delete()
    # Deleta o equipamento
    equipamento.delete()
    
    messages.add_message(request, constants.ERROR,
                         'Equipamento deletado com sucesso!')
    return redirect(reverse('equipamentos'))

# Extrair Forms do Equipamento
def extrair_forms_equipamento(request):
    codigo_sharepoint = request.POST.get('codigo_sharepoint')
    setor = request.POST.get('setor')
    configuracao = request.POST.get('configuracao')
    serial_windows = request.POST.get('serial_windows')
    serial_office = request.POST.get('serial_office')
    ip = request.POST.get('ip')
    mac_address = request.POST.get('mac_address')
    patrimonio = request.POST.get('patrimonio')
    numero_serie = request.POST.get('numero_serie')
    tipo = request.POST.get('tipo')
    responsavel = request.POST.get('responsavel')
    status = request.POST.get('status')
    descricao = request.POST.get('descricao')
    imagens = request.FILES.getlist('imagens')

    equipamento = Equipamento(
        codigo_sharepoint=codigo_sharepoint,
        setor=Setor(id=setor),
        configuracao=configuracao,
        serial_windows=serial_windows,
        serial_office=serial_office,
        ip=ip,
        mac_address=mac_address,
        patrimonio=patrimonio,
        numero_serie=numero_serie,
        tipo=tipo,
        responsavel=responsavel,
        status=status,
        descricao=descricao,
    )

    equipamento.save()
    
    if imagens is not None:
        convert_imagem(imagens, equipamento.id)

    messages.add_message(request, messages.SUCCESS,
                         'Equipamento Inserido com Sucesso!')
    return redirect(reverse('add_equipamento'))



# Converter Imagens
def convert_imagem(imagens, fk):
    equipamento = Equipamento.objects.get(id=fk)
    for fimg in imagens:
        name = f'{equipamento.id}-{equipamento.indentificador}.jpg'
        # Tratamento da imagem
        img = Image.open(fimg)
        img = img.convert('RGB')
        img = img.resize((800, 600))
        draw = ImageDraw.Draw(img)
        draw.text((20, 580), "PREFEITURA MUNICIPAL DE NOVO HORIZONTE",
                  (255, 255, 255))
        output = BytesIO()
        img.save(output, format="JPEG", quality=100)
        output.seek(0)
        img_render = InMemoryUploadedFile(
            output,
            'ImageField',
            name,
            'image/jpeg',
            sys.getsizeof(output),
            None
        )

        img_final = Imagem(imagem=img_render, equipamento=equipamento)
        img_final.save()

# ----------------------------------------------------------------
#                         IMAGEMS                                #
# ----------------------------------------------------------------
def insImagens(request, fk):
    if request.method == 'POST':
        imagens = request.FILES.getlist('imagens')
        convert_imagem(imagens, fk)
        messages.add_message(request, messages.SUCCESS,
                             'Imagens Inseridas com Sucesso!')
        return redirect(reverse('view_equipamento', kwargs={'id': fk}))


def delImagem(request, id, fk):
    imagem = Imagem.objects.get(id=id)
    imagem.delete()
    messages.add_message(request, messages.ERROR,
                         'Imagem excluida com sucesso!')
    return redirect(reverse('view_equipamento', kwargs={'id': fk}))


def upEquipamento(request, id):
    equipamento = Equipamento.objects.get(id=id)
    context = {
        'equipamento': equipamento,
    }
    return render(request, 'update_equipamento.html', context)
