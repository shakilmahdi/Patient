from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from home import models as homeModel




class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ContactForm(ModelForm):
	class Meta:
		model = homeModel.Contact
		fields = '__all__'

	def clean(self):
		cleaned_data = super().clean()
		name = cleaned_data.get('name')
		if  homeModel.Contact.objects.filter(name=name).exists():
			self.add_error('name', 'Username already exists')


class HomePatientForm(ModelForm):
	class Meta:
		model = homeModel.Patient
		fields = '__all__' 

	def clean(self):
		cleaned_data = super().clean()
		patient_national_ID = cleaned_data.get('patient_national_ID')
		if  homeModel.Patient.objects.filter(patient_national_ID=patient_national_ID).exists():
			self.add_error('patient_national_ID', 'Username already exists')


class IndoorAdmissionForm(ModelForm):
	class Meta:
		model = homeModel.IndoorPatient
		fields = '__all__' 
		
	def clean(self):
		cleaned_data = super().clean()
		Active = "Active"
		Pending ="Pending"
		Re_Admitted = "Re_Admitted"
		Admission ="Admission"

		patient_national_ID = cleaned_data.get('patient_national_ID')
		indoor_treatment_patient_id=cleaned_data.get('indoor_treatment_patient_id')
		indoor_treatment_patient_status = cleaned_data.get('indoor_treatment_patient_status')
		indoor_treatment_patient_type = cleaned_data.get('indoor_treatment_patient_type')
		

		if homeModel.IndoorPatient.objects.filter(patient_national_ID= patient_national_ID).exists():
			if homeModel.IndoorPatient.objects.filter(indoor_treatment_patient_id=indoor_treatment_patient_id):
				print('ok')
			else:
				self.add_error('indoor_treatment_patient_status', 'Patient already exists')
	
		# if ((homeModel.IndoorPatient.objects.filter(indoor_treatment_patient_type= Re_Admitted))):
		# 		if ((homeModel.IndoorPatient.objects.filter(indoor_treatment_patient_status= 'Active'))|( homeModel.IndoorPatient.objects.filter(indoor_treatment_patient_status='Pending'))) :
		# 			self.add_error('indoor_treatment_patient_status', 'Username already Active')

		
		# 	# if  homeModel.Patient.objects.filter(patient_national_ID=patient_national_ID).exists():
		# 	# 	self.add_error('patient_national_ID', 'Username already exists')
		
		# if ((homeModel.IndoorPatient.objects.filter(indoor_treatment_patient_type= 'Admitted'))):
		# 	if homeModel.IndoorPatient.objects.filter(indoor_treatment_patient_id=indoor_treatment_patient_id).exists():
		# 		print('ok')
	

class OutdoorDoctorForm(ModelForm):
	class Meta:
		model = homeModel.OutdoorPatient
		fields = '__all__'

	
	def clean(self):
		cleaned_data = super().clean()
		phone = cleaned_data.get('phone')
		doctor = cleaned_data.get('doctor')
		date = cleaned_data.get('date')
		if  homeModel.OutdoorPatient.objects.filter(phone=phone).exists():
			self.add_error('phone', 'Username already exists')
		
		
		# serial_number =  homeModel.OutdoorPatient.objects.filter(doctor=doctor).count()+1
		# a=serial_number
		# print(a)
		

class AddReportForm(ModelForm):
	class Meta:
		model = homeModel.AddReport
		fields = '__all__'

class AddIpReportForm(ModelForm):
	class Meta:
		model = homeModel.AddIpReport
		fields = '__all__'

class HpAppointmentForm(ModelForm):
	class Meta:
		model = homeModel.Appointment
		fields = '__all__'