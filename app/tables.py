import django_tables2 as tables
from .models import Valuebase
from django_tables2_column_shifter.tables import ColumnShiftTable


class ValuebaseTable(tables.Table):
    class Meta:
        model = Valuebase
        template_name = "django_tables2/bootstrap.html"
        fields = ('date', 'id_bt', 'id_city', 'id_office', 'id_group', 'id_indicator', 'value')

class ResultsTable(tables.Table):
    class Meta:
        model = Valuebase
        template_name = "django_tables2/bootstrap.html"
        fields = ('id_bt', 'id_city', 'id_office', 'id_group', 'id_indicator', 'value')
