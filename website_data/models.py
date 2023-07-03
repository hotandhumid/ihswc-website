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

    category1 = models.CharField(max_length=100)
    title1 = models.CharField(max_length=100)
    word_count1 = models.CharField(max_length=100)
    pdf_file1 = models.FileField()

    category2 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    word_count2 = models.CharField(max_length=100)
    pdf_file2 = models.FileField()

    category3 = models.CharField(max_length=100)
    title3 = models.CharField(max_length=100)
    word_count3 = models.CharField(max_length=100)
    pdf_file3 = models.FileField()

    category4 = models.CharField(max_length=100)
    title4 = models.CharField(max_length=100)
    word_count4 = models.CharField(max_length=100)
    pdf_file4 = models.FileField()

    category5 = models.CharField(max_length=100)
    title5 = models.CharField(max_length=100)
    word_count5 = models.CharField(max_length=100)
    pdf_file5 = models.FileField()


    student_checkbox = models.BooleanField()
    teacher_checkbox = models.BooleanField()


    def __str__(self):
        return f"{str(self.firstname).capitalize()} {str(self.lastname).capitalize()}'s Submission|"

    class Meta:
        verbose_name = "Student Submission"
