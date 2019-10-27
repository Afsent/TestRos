from django import forms


class ValuebaseFilterForm(forms.Form):
    bt = forms.CharField(label='ТО', required=False)
    city = forms.CharField(label='Город', required=False)
    office = forms.IntegerField(label='Номер офиса', required=False)
    min_value = forms.IntegerField(label='От', required=False)
    max_value = forms.IntegerField(label='До', required=False)
    min_date = forms.DateField(label='От', widget=forms.widgets.SelectDateWidget())
    max_date = forms.DateField(label='До', widget=forms.widgets.SelectDateWidget())
    bt_res = forms.CharField(label='ТО', required=False)
    city_res = forms.CharField(label='Город', required=False)
    office_res = forms.IntegerField(label='Номер офиса', required=False)
    min_date_res = forms.DateField(widget=forms.widgets.SelectDateWidget())
    max_date_res = forms.DateField(widget=forms.widgets.SelectDateWidget())

