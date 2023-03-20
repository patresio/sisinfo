from django.contrib import admin
from equipamentos.models import Equipamento

# Register your models here.


class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ['indentificador',
                    'codigo_sharepoint', 'patrimonio', 'setor', 'numero_serie', 'responsavel', 'serial_windows', 'serial_office', 'mac_address']
    search_fields = ['indentificador',
                     'patrimonio', 'codigo_sharepoint', 'serial_windows', 'serial_office', 'mac_address', 'responsavel', 'numero_serie']
    list_per_page = 10


admin.site.register(Equipamento, EquipamentoAdmin)
