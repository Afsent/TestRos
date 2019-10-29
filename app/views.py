from datetime import date
from django.shortcuts import render
from .models import Valuebase
from django_tables2 import RequestConfig
from .tables import ValuebaseTable
from .forms import ValuebaseFilterForm, ResForm
from django.db.models import Avg, Max, Min, Count
from qsstats import QuerySetStats


def get_stat(res, ind, max_date, min_date):
    result = res.filter(id_indicator=ind).filter(date=max_date).aggregate(Avg('value')).get(
        'value__avg') / res.filter(id_indicator=ind).filter(
        date=min_date).aggregate(Avg('value')).get('value__avg')
    return result


def get_stat_def(res, ind):
    result = res.filter(id_indicator=ind).aggregate(Avg('value')).get('value__avg') / res.filter(
        id_indicator=ind).aggregate(Avg('value')).get(
        'value__avg')
    return result


def valuebase(request):
    # формирование данных (таблица + фильтр)
    form = ValuebaseFilterForm(request.POST)
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

    # формирование таблицы показателей
    res_form = ResForm(request.POST)
    res = Valuebase.objects.all()
    min_date = date(2019, 1, 1)
    max_date = date.today()
    if res_form.is_valid():
        if res_form.cleaned_data['bt_res']:
            res = res.filter(id_bt__name=res_form.cleaned_data['bt_res'])

        if res_form.cleaned_data['city_res']:
            res = res.filter(id_city__city=res_form.cleaned_data['city_res'])

        if res_form.cleaned_data['office_res']:
            res = res.filter(id_office__office=res_form.cleaned_data['office_res'])

        if res_form.cleaned_data['min_date_res']:
            res = res.filter(date__gte=res_form.cleaned_data['min_date_res'])
            # проверка на существование записей с минимальной датой
            if res_form.cleaned_data['min_date_res'] < values.aggregate(Min('date')).get('date__min'):
                min_date = values.aggregate(Min('date')).get('date__min')
            else:
                min_date = res_form.cleaned_data['min_date_res']

        if res_form.cleaned_data['max_date_res']:
            res = res.filter(date__lte=res_form.cleaned_data['max_date_res'])
            # проверка на существование записей с максимальной датой
            if res_form.cleaned_data['max_date_res'] > values.aggregate(Max('date')).get('date__max'):
                max_date = values.aggregate(Max('date')).get('date__max')
            else:
                max_date = res_form.cleaned_data['max_date_res']

        # вычисляем отношение показателя "Активные клиенты"
        act_clients = get_stat(res, 1, max_date, min_date)
        # вычисляем отношение показателя "Кредитные карты"
        credit_cards = get_stat(res, 2, max_date, min_date)
        # вычисляем отношение показателя "Costs"
        costs = get_stat(res, 3, max_date, min_date)
        # вычисляем отношение показателя "NBI"
        nbi = get_stat(res, 4, max_date, min_date)
    else:
        # задаем начальные значения для показателей, если форма не заполнена
        act_clients = get_stat_def(res, 1)
        credit_cards = get_stat_def(res, 2)
        costs = get_stat_def(res, 3)
        nbi = get_stat_def(res, 4)

    # формирование диаграммы

    start_date = min_date
    end_date = max_date
    queryset = Valuebase.objects.values_list('date', 'value')
    qss = QuerySetStats(queryset, date_field='date', aggregate=Avg('value'))  # вычисление среднего значения показателей
    graph = qss.time_series(start_date, end_date, interval='months')            # за указанный период

    return render(request, 'valuebase.html',
                  {'valuebase': table, 'form': form, 'res_form': res_form, 'act_clients': round(act_clients * 100),
                   'credit_cards': round(credit_cards * 100), 'costs': round(costs * 100), 'nbi': round(nbi * 100),
                   'graph': graph, 'queryset': qss.__dict__})
