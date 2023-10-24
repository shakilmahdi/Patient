# Generated by Django 4.1.4 on 2023-01-31 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddIpReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indoor_treatment_patient_id', models.CharField(max_length=122)),
                ('r_name', models.CharField(max_length=122)),
                ('r_type', models.CharField(max_length=122)),
                ('report_file', models.FileField(upload_to='')),
                ('report_description', models.CharField(blank=True, max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='AddReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=122)),
                ('r_name', models.CharField(max_length=122)),
                ('r_type', models.CharField(max_length=122)),
                ('report_file', models.FileField(upload_to='')),
                ('report_description', models.CharField(blank=True, max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=122)),
                ('transaction_phone', models.CharField(max_length=122)),
                ('transaction_id', models.CharField(max_length=122)),
                ('ap_date', models.DateField()),
                ('ap_doctor', models.CharField(max_length=122)),
                ('Phone', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IndoorPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indoor_treatment_patient_type', models.CharField(max_length=122)),
                ('indoor_treatment_patient_id', models.CharField(max_length=122)),
                ('indoor_treatment_patient_status', models.CharField(blank=True, max_length=122)),
                ('patient_name', models.CharField(max_length=122)),
                ('patient_age', models.CharField(max_length=122)),
                ('patient_gender', models.CharField(max_length=122)),
                ('patient_phone', models.CharField(max_length=122)),
                ('patient_email', models.CharField(max_length=122)),
                ('patient_national_ID', models.CharField(max_length=122)),
                ('indoor_patient_bed_bed_id', models.CharField(blank=True, max_length=122)),
                ('indoor_bed_price', models.CharField(max_length=122)),
                ('indoor_patient_bed_entry_time', models.CharField(max_length=122)),
                ('indoor_patient_bed_discharge_time', models.CharField(blank=True, max_length=122)),
                ('bed_total_bill', models.CharField(blank=True, max_length=122)),
                ('indoor_patient_doctor_doctor_id', models.CharField(max_length=122)),
                ('doctor_visit_fee', models.CharField(max_length=122)),
                ('doctor_total_bill', models.CharField(max_length=122)),
                ('outdoor_service_id', models.CharField(max_length=122)),
                ('outdoor_service_rate', models.CharField(max_length=122)),
                ('indoor_treatment_total_bill', models.CharField(max_length=122)),
                ('indoor_treatment_total_paid', models.CharField(blank=True, max_length=122)),
                ('indoor_treatment_total_due', models.CharField(blank=True, max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notesfile', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='OutdoorPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('branch', models.CharField(max_length=122)),
                ('doctor', models.CharField(max_length=122)),
                ('name', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('age', models.CharField(max_length=122)),
                ('gender', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_type', models.CharField(max_length=122)),
                ('patient_id', models.CharField(max_length=122)),
                ('patient_date', models.DateField(blank=True)),
                ('patient_name', models.CharField(blank=True, max_length=122)),
                ('patient_gender', models.CharField(blank=True, max_length=122)),
                ('patient_age', models.CharField(blank=True, max_length=122)),
                ('patient_phone', models.CharField(blank=True, max_length=122)),
                ('patient_email', models.CharField(blank=True, max_length=122)),
                ('patient_dob', models.CharField(max_length=122)),
                ('patient_blood_group', models.CharField(blank=True, max_length=122)),
                ('patient_national_ID', models.CharField(blank=True, max_length=122)),
                ('patient_address', models.CharField(blank=True, max_length=122)),
                ('patient_emergency_name', models.CharField(max_length=122)),
                ('patient_emergency_relation', models.CharField(blank=True, max_length=122)),
                ('patient_emergency_contact', models.CharField(max_length=122)),
                ('patient_emergency_address', models.CharField(blank=True, max_length=122)),
            ],
        ),
    ]
