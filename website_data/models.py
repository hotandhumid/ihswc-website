
from django.db import models


# Create your models here.

class TestFileModel(models.Model):
    firstname = models.CharField(default="___", max_length=100)
    lastname = models.CharField(default="___", max_length=100)
    email = models.CharField(default="___", max_length=100)
    phone_number = models.CharField(default="___", max_length=100)
    country = models.CharField(default="___", max_length=100)
    city = models.CharField(default="___", max_length=100)
    zipcode = models.CharField(default="___", max_length=100)
    grade_level = models.CharField(default="___", max_length=100)
    birthday = models.DateField(default="1990-01-01")
    school_name = models.CharField(default="___", max_length=100)
    school_address = models.CharField(default="___", max_length=100)
    parent_firstname = models.CharField(default="___", max_length=100)
    parent_lastname = models.CharField(default="___", max_length=100)
    parent_email = models.CharField(default="___", max_length=100)
    parent_phone_number = models.CharField(default="___", max_length=100)

    category1 = models.CharField(default="___", max_length=100)
    title1 = models.CharField(default="___", max_length=100)
    word_count1 = models.CharField(default="___", max_length=100)
    pdf_file1 = models.FileField(default="___")

    category2 = models.CharField(default="___", max_length=100)
    title2 = models.CharField(default="___", max_length=100)
    word_count2 = models.CharField(default="___", max_length=100)
    pdf_file2 = models.FileField(default="___")

    category3 = models.CharField(default="___", max_length=100)
    title3 = models.CharField(default="___", max_length=100)
    word_count3 = models.CharField(default="___", max_length=100)
    pdf_file3 = models.FileField(default="___")

    category4 = models.CharField(default="___", max_length=100)
    title4 = models.CharField(default="___", max_length=100)
    word_count4 = models.CharField(default="___", max_length=100)
    pdf_file4 = models.FileField(default="___")

    category5 = models.CharField(default="___", max_length=100)
    title5 = models.CharField(default="___", max_length=100)
    word_count5 = models.CharField(default="___", max_length=100)
    pdf_file5 = models.FileField(default="___")

    def __str__(self):
        return f"{str(self.firstname).capitalize()} {str(self.lastname).capitalize()}'s Submission"
    
    class Meta:
        verbose_name = "Student Submission"

