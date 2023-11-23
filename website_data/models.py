
from django.db import models


# Create your models here.


class JudgeModel(models.Model):
    graded_by = models.CharField(max_length=50)
    review = models.CharField(max_length=300)
    rating = models.CharField(max_length=5)
    submission = models.CharField(max_length=5)

    def get_values(self):
        return {
            "graded_by": self.graded_by,
            "review": self.review,
            "rating": self.rating, 
            "submission": self.submission
        }
    
    def __str__(self):
        return f"Submission {self.submission} graded by {self.graded_by}"

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

    def get_values(self):
        return {
                "firstname": self.firstname,
                "lastname": self.lastname,
                "email": self.email,
                "phone_number": self.phone_number,
                "country": self.country,
                "city": self.city,
                "zipcode": self.zipcode,
                "grade_level": self.grade_level,
                "birthday": self.birthday,
                "school_name": self.school_name,
                "school_address": self.school_address,
                "parent_firstname": self.parent_firstname,
                "parent_lastname": self.parent_lastname,
                "parent_email": self.parent_email,
                "parent_phone_number": self.parent_phone_number,

                "category1": self.category1,
                "title1": self.title1,
                "word_count1": self.word_count1,
                "pdf_file1": self.pdf_file1,

                "category2": self.category2,
                "title2": self.title2,
                "word_count2": self.word_count2,
                "pdf_file2": self.pdf_file2,

                "category3": self.category3,
                "title3": self.title3,
                "word_count3": self.word_count3,
                "pdf_file3": self.pdf_file3,

                "category4": self.category4,
                "title4": self.title4,
                "word_count4": self.word_count4,
                "pdf_file4": self.pdf_file4,

                "category5": self.category5,
                "title5": self.title5,
                "word_count5": self.word_count5,
                "pdf_file5": self.pdf_file5,
        }

    def __str__(self):
        return f"{str(self.firstname).capitalize()} {str(self.lastname).capitalize()}'s Submission"
    
    class Meta:
        verbose_name = "Student Submission"

