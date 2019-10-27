from django.shortcuts import render
from .models import Valuebase
from django_tables2 import RequestConfig
from .tables import ValuebaseTable
from .forms import ValuebaseFilterForm
from django.db.models import Avg, Max, Min

def valuebase(request):
    form = ValuebaseFilterForm(request.GET)
    values = Valuebase.objects.all()
    if form.is_valid():
        if form.cleaned_data['min_value']:
            values = values.filter(value__gte=form.cleaned_data['min_value'])

        if form.cleaned_data['max_value']:
            values = values.filter(value__lte=form.cleaned_data['max_value'])

        if form.cleaned_data['min_date']:
            values = values.filter(date__gte=form.cleaned_data['min_date'])

        if form.cleaned_data['max_date']:
            values = values.filter(date__lte=form.cleaned_data['max_date'])

        if form.cleaned_data['bt']:
            values = values.filter(id_bt__name=form.cleaned_data['bt'])

        if form.cleaned_data['office']:
            values = values.filter(id_office__office=form.cleaned_data['office'])

        if form.cleaned_data['city']:
            values = values.filter(id_city__city=form.cleaned_data['city'])
    table = ValuebaseTable(values)
    RequestConfig(request).configure(table)

    res = Valuebase.objects.all()
    act_clients = res.filter(id_indicator=1)
    if form.is_valid():
        if form.cleaned_data['bt_res']:
            res = res.filter(id_bt__name=form.cleaned_data['bt_res'])

        if form.cleaned_data['city_res']:
            res = res.filter(id_city__city=form.cleaned_data['city_res'])

        if form.cleaned_data['office_res']:
            res = res.filter(id_office__office=form.cleaned_data['office_res'])

        if form.cleaned_data['min_date_res']:
            res = res.filter(date__gte=form.cleaned_data['min_date_res'])

        if form.cleaned_data['max_date_res']:
            res = res.filter(date__lte=form.cleaned_data['max_date_res'])

    act_clients = act_clients.filter(id_indicator=1).filter(date=form.cleaned_data['max_date_res']).aggregate(Avg('value'))
                      #res.filter(id_indicator=1).filter(date=form.cleaned_data['max_date_res'])
    return render(request, 'valuebase.html', {'valuebase': table, 'form': form, 'results': res, 'act_clients': act_clients})
