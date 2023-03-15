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

from .models import Equipamento
from .forms import EquipamentoForm



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
