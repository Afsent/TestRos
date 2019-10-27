from django.contrib import admin

# Register your models here.
from .models import Bt, Valuebase, Cities, Groupindicators, Indicators, Offices

# Register the Admin classes for Bt using the decorator
@admin.register(Bt)
class BtAdmin(admin.ModelAdmin):
    list_display = ('id_bt', 'name')

# Register the Admin classes for ValueBase using the decorator
@admin.register(Valuebase)
class ValuebaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'id_bt', 'id_city', 'id_office', 'id_group', 'id_indicator', 'value')
    fields = ['id', ('id_bt', 'id_city', 'id_office'), ('id_group', 'id_indicator'), ('date', 'value')]
    list_filter = ('date', 'id_bt', 'id_city', 'id_office', 'id_group', 'id_indicator')

# Register the Admin classes for Cities using the decorator
@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('id_city', 'id_bt', 'city')
    list_filter = ('id_bt',)

# Register the Admin classes for Offices using the decorator
@admin.register(Offices)
class OfficesAdmin(admin.ModelAdmin):
    list_display = ('id_office', 'id_city', 'office')
    list_filter = ('id_city',)


# Register the Admin classes for Groupindicators using the decorator
@admin.register(Groupindicators)
class GroupindicatorsAdmin(admin.ModelAdmin):
    list_display = ('id_group', 'name')

# Register the Admin classes for Indicators using the decorator
@admin.register(Indicators)
class IndicatorsAdmin(admin.ModelAdmin):
    list_display = ('id_indicator','id_group', 'indicator')
    list_filter = ('id_group',)
