from django import forms
from .models import Bt

# форма фильтра для таблицы
class ValuebaseFilterForm(forms.Form):
    bt = forms.ModelChoiceField(queryset=Bt.objects.all(), label='ТО', required=False)
    city = forms.CharField(label='Город', required=False)
    office = forms.IntegerField(label='Номер офиса', required=False)
    min_value = forms.IntegerField(label='Минимальное значение', required=False)
    max_value = forms.IntegerField(label='Максимальное значение', required=False)
    min_date = forms.DateField(label='От', widget=forms.widgets.SelectDateWidget(years=range(2012, 2020)))
    max_date = forms.DateField(label='До', widget=forms.widgets.SelectDateWidget(years=range(2012, 2020)))

# форма таблицы с показателями эфективности
class ResForm(forms.Form):
    bt_res = forms.CharField(label='ТО', required=False)
    city_res = forms.CharField(label='Город', required=False)
    office_res = forms.IntegerField(label='Номер офиса', required=False)
    min_date_res = forms.DateField(label='От', widget=forms.widgets.SelectDateWidget(years=range(2012, 2020)))
    max_date_res = forms.DateField(label='До', widget=forms.widgets.SelectDateWidget(years=range(2012, 2020)))

