from django.db import models


class Registration(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    cpassword = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Registration'
        verbose_name_plural = 'Registration'

    def __str__(self):
        return self.username


class Login(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Login'
        verbose_name_plural = 'Login'

    def __str__(self):
        return self.username


class AdmissionPage(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50, null=True, blank=True)
    mob = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    department = models.CharField(max_length=50, null=True, blank=True)
    courses = models.CharField(max_length=50, null=True, blank=True)
    purposes = models.CharField(max_length=50, null=True, blank=True)
    materials = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'formPage'
        verbose_name_plural = 'formPage'

    def __str__(self):
        return self.email

# Create your models here.
