from django.db import models

# Create your models here.

class CreateUserModel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=100)
    birthday = models.DateField()
    school_name = models.CharField(max_length=100)
    school_address = models.CharField(max_length=100)
    pdf_id = models.FileField()
    parent_firstname = models.CharField(max_length=100)
    parent_lastname = models.CharField(max_length=100)
    parent_email = models.CharField(max_length=100)
    parent_phone_number = models.CharField(max_length=100)

    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    word_count = models.CharField(max_length=100)
    pdf_file = models.FileField()

    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    word_count = models.CharField(max_length=100)
    pdf_file = models.FileField()

    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    word_count = models.CharField(max_length=100)
    pdf_file = models.FileField()

    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    word_count = models.CharField(max_length=100)
    pdf_file = models.FileField()

    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    word_count = models.CharField(max_length=100)
    pdf_file = models.FileField()


    student_checkbox = models.BooleanField()
    teacher_checkbox = models.BooleanField()
