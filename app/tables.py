from .models import Valuebase
from django_tables2_column_shifter.tables import ColumnShiftTable

# ColumnShiftTable - класс для отображения/скрытия определенных данных в таблице
class ValuebaseTable(ColumnShiftTable):
    class Meta:
        model = Valuebase
        template_name = "django_tables2/bootstrap.html"
        fields = ('date', 'id_bt', 'id_city', 'id_office', 'id_group', 'id_indicator', 'value')

