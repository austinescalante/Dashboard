from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Add an author to patient for posts


class Patient(models.Model):
    PatientID = models.IntegerField()
    PatientSSN = models.CharField(max_length=30)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Address = models.TextField(max_length=200)
    Sex = models.CharField(max_length=1)
    DOB = models.DateField(default=timezone.now)

    # Shows the Object in the Query set after the object is saved into Database
    def __str__(self):
        return self.FirstName

    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk': self.pk})


class Employee(models.Model):
    EmployeeID = models.IntegerField(primary_key=True)
    EmployeeSSN = models.CharField(max_length=30)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Address = models.TextField(max_length=200)
    Sex = models.CharField(max_length=1)


class Doctor(models.Model):
    DoctorID = models.IntegerField(primary_key=True)
    EID = models.IntegerField()
    Qualifications = models.TextField(max_length=100)
    Speciality = models.TextField(max_length=100)
    DOB = models.DateField(default=timezone.now)
    EID = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Nurse(models.Model):
    NurseID = models.IntegerField(primary_key=True)
    EID = models.IntegerField()
    Qualifications = models.TextField(max_length=100)
    Speciality = models.TextField(max_length=100)
    DOB = models.DateField(default=timezone.now)
    EID = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Patient_VisitHistory(models.Model):
    VisitedID = models.IntegerField(primary_key=True)
    PID = models.IntegerField()
    VisitDate = models.DateField(default=timezone.now)
    DID = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Doctor_VisitHistory(models.Model):
    VID = models.IntegerField(primary_key=True)
    DID = models.IntegerField(primary_key=True)
    DID = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Nurse_VisitHistory(models.Model):
    NID = models.IntegerField(primary_key=True)
    DID = models.IntegerField(primary_key=True)
    NID = models.ForeignKey(Nurse, on_delete=models.CASCADE)


class Patient_Bill(models.Model):
    PID = models.IntegerField(primary_key=True)
    BillID = models.IntegerField(primary_key=True)
    BillDate = models.DateField(default=timezone.now)
    TotalCost = models.CharField(max_length=20)
    PID = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Patient_PhoneNumbers:
    PID = models.IntegerField(primary_key=True)
    PhoneNumber = models.CharField(max_length=12)
    PID = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Patient_Doctor:
    PID = models.IntegerField(primary_key=True)
    DID = models.IntegerField(primary_key=True)
    PID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    DID = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Patient_Nurse:
    PID = models.IntegerField(primary_key=True)
    NID = models.IntegerField(primary_key=True)
    PID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    NID = models.ForeignKey(Nurse, on_delete=models.CASCADE)
