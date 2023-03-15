from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants

from secrets import token_urlsafe

from PIL import Image, ImageDraw
from datetime import date
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


# Create your views here.

from .models import Equipamento
from .forms import EquipamentoForm
from dashboard.models import ImagemAlbum, Imagem


def addEquipamentos(request):        
    form = EquipamentoForm()
    context = {
        'form': form,
    }
    return render(request, 'cadEquipamentos.html', context)


def equipamentos(request):
    equipamentos = Equipamento.objects.all()
    context = {
        'equipamentos': equipamentos,
    }
    return render(request, 'equipamentos.html', context)

def addImagens(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_album')
        imagens = request.FILES.getlist('imagens')
        album = ImagemAlbum(
            name = nome,
        )
        print(nome)
        album.save()
        print(album.id)
        for fimg in imagens:
            name = f'{token_urlsafe(16)}-album-{album.id}.jpg'
            img = Image.open(fimg)
            img = img.convert('RGB')
            img = img.resize((300, 300))
            draw = ImageDraw.Draw(img)
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

            img_final = Imagem(
                name = name,
                image = img_render,
                default = False,
                width = 300,
                length = 300,
                album = album.id,
            )

            img_final.save()

        messages.add_message(request, messages.SUCCESS, f'Imagens cadastradas com sucesso!{album}')
    else:
        messages.add_message(request, messages.ERROR, 'Ocorreu um erro no cadastro das imagens!')
    return redirect(reverse('add_equipamento'))