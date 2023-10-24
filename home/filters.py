import django_filters
from django_filters import DateFilter
# from .model import *

class IndoorPatientFilter(django_filters.filterset):
    start_date = DataFilter(field_name="indoor_patient_bed_entry_time", lookup_expr='gte')

    start_date = DataFilter(field_name="indoor_patient_bed_entry_time", lookup_expr='lte')
    class Meta:
        model = IndoorPatient
        fields='__all__'
        exclude = ['indoor_patient_bed_entry_time']
