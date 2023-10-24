from django.contrib import admin
from home.models import Contact
from home.models import Patient
from home.models import IndoorPatient
from home.models import OutdoorPatient
from home.models import Appointment
from home.models import AddReport
from home.models import AddIpReport
# from home.models import User

# class ContactAdmin(admin.ModelAdmin):
#     list_display=('name','email','address','phone','message')

# class PatientAdmin(admin.ModelAdmin):
#      list_display=('branch', 'speciality','doctor','notes','name','phone','age','gender')

# class OutdoorPatientAdmin(admin.ModelAdmin):
#      list_display=('patient_name', 'patient_gender','patient_age','patient_phone','patient_email','patient_dob','patient_blood_group','patient_national_ID','patient_marital_status','patient_guardian','patient_refered_by','patient_description','patient_address','patient_emergency_name','patient_emergency_relation','patient_emergency_contact','patient_emergency_address')

# class IndoorPatientAdmin(admin.ModelAdmin):
#      list_display=('indoor_treatment_patient_id','patient_name','patient_gender','patient_age','patient_phone','indoor_bed_category_name','indoor_patient_bed_bed_id','indoor_bed_price','indoor_patient_bed_entry_time','indoor_patient_bed_discharge_time','bed_total_bill','indoor_patient_doctor_doctor_id','doctor_specialization','doctor_visit_fee','doctor_total_bill','indoor_service_id','indoor_service_rate','indoor_treatment_total_bill','indoor_treatment_discount_pc','indoor_treatment_total_bill_after_discount','indoor_treatment_total_paid','indoor_treatment_total_due','indoor_treatment_payment_type','indoor_treatment_payment_type_no','indoor_treatment_note')
# Register your models here.
admin.site.register(Contact)
admin.site.register(Patient )
admin.site.register(IndoorPatient )
admin.site.register(OutdoorPatient )
admin.site.register(Appointment)
admin.site.register(AddReport)
admin.site.register(AddIpReport)
