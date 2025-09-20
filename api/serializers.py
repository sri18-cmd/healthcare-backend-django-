from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user

class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Patient
        fields = ['id', 'name', 'date_of_birth', 'address', 'phone_number', 'created_by']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'phone_number']

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'patient_name', 'doctor_name']