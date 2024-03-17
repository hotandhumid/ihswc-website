
from django.db import models


# Create your models here.


class JudgeModel1(models.Model):
    graded_by = models.CharField(max_length=50)
    review = models.CharField(max_length=300, default='', null=True, blank=True)
    rating = models.CharField(max_length=5)
    submission = models.CharField(max_length=5, default='', null=True, blank=True)
    sub_number = models.CharField(max_length=5, default='', null=True, blank=True)

    def get_values(self):
        return {
            "graded_by": self.graded_by,
            "review": self.review,
            "rating": self.rating, 
            "submission": self.submission
        }
    
    def __str__(self):
        return f"Submission {self.submission} graded by {self.graded_by}"


class JudgeModel2(models.Model):
    graded_by = models.CharField(max_length=50)
    review = models.CharField(max_length=300, default='', null=True, blank=True)
    rating = models.CharField(max_length=5)
    submission = models.CharField(max_length=5, default='', null=True, blank=True)
    sub_number = models.CharField(max_length=5, default='', null=True, blank=True)

    def get_values(self):
        return {
            "graded_by": self.graded_by,
            "review": self.review,
            "rating": self.rating, 
            "submission": self.submission
        }

    def __str__(self):
        return f"Submission {self.submission} graded by {self.graded_by}"


class JudgeModel3(models.Model):
    graded_by = models.CharField(max_length=50)
    review = models.CharField(max_length=300, default='', null=True, blank=True)
    rating = models.CharField(max_length=5)
    submission = models.CharField(max_length=5, default='', null=True, blank=True)
    sub_number = models.CharField(max_length=5, default='', null=True, blank=True)

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
    firstname = models.CharField(default="___", max_length=100, blank=True)
    lastname = models.CharField(default="___", max_length=100, blank=True)
    email = models.CharField(default="___", max_length=100, blank=True)
    phone_number = models.CharField(default="___", max_length=100, blank=True)
    country = models.CharField(default="___", max_length=100, blank=True)
    city = models.CharField(default="___", max_length=100, blank=True)
    zipcode = models.CharField(default="___", max_length=100, blank=True)
    grade_level = models.CharField(default="___", max_length=100, blank=True)
    birthday = models.DateField(default="1990-01-01", blank=True)
    school_name = models.CharField(default="___", max_length=100, blank=True)
    school_address = models.CharField(default="___", max_length=100, blank=True)
    parent_firstname = models.CharField(default="___", max_length=100, blank=True)
    parent_lastname = models.CharField(default="___", max_length=100, blank=True)
    parent_email = models.CharField(default="___", max_length=100, blank=True)
    parent_phone_number = models.CharField(default="___", max_length=100, blank=True)

    category1 = models.CharField(default="___", max_length=100, blank=True)
    title1 = models.CharField(default="___", max_length=100, blank=True)
    word_count1 = models.CharField(default="___", max_length=100, blank=True)
    pdf_file1 = models.FileField(default="___", blank=True)

    category2 = models.CharField(default="___", max_length=100, blank=True)
    title2 = models.CharField(default="___", max_length=100, blank=True)
    word_count2 = models.CharField(default="___", max_length=100, blank=True)
    pdf_file2 = models.FileField(default="___", blank=True)

    category3 = models.CharField(default="___", max_length=100, blank=True)
    title3 = models.CharField(default="___", max_length=100, blank=True)
    word_count3 = models.CharField(default="___", max_length=100, blank=True)
    pdf_file3 = models.FileField(default="___", blank=True)

    category4 = models.CharField(default="___", max_length=100, blank=True)
    title4 = models.CharField(default="___", max_length=100, blank=True)
    word_count4 = models.CharField(default="___", max_length=100, blank=True)
    pdf_file4 = models.FileField(default="___", blank=True)

    category5 = models.CharField(default="___", max_length=100, blank=True)
    title5 = models.CharField(default="___", max_length=100, blank=True)
    word_count5 = models.CharField(default="___", max_length=100, blank=True)
    pdf_file5 = models.FileField(default="___", blank=True)

    judge_model1 = models.OneToOneField(
        JudgeModel1, related_name="test_file_model", on_delete=models.SET_NULL, null=True, blank=True, default=None
    )

    judge_model2 = models.OneToOneField(
        JudgeModel2, related_name="test_file_model", on_delete=models.SET_NULL, null=True, blank=True, default=None
    )

    judge_model3 = models.OneToOneField(
        JudgeModel3, related_name="test_file_model", on_delete=models.SET_NULL, null=True, blank=True, default=None
    )

    average_rating = models.FloatField(null=True, blank=True, default=None)     # Field to store average rating
    all_judges_filled = models.BooleanField(default=False)
    is_email_notified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    AWARD_CATEGORIES = (
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
        ('honor', 'Honor'),
        ('no_award', 'No Award'),
    )

    # New field for award category
    award = models.CharField(
        max_length=10,
        choices=AWARD_CATEGORIES,
        default='no_award',
        blank=True,
        help_text="Select the award category"
    )

    def calculate_average_rating(self):
        ratings = []
        for judge_model in [self.judge_model1, self.judge_model2, self.judge_model3]:
            if judge_model and judge_model.rating:
                try:
                    ratings.append(float(judge_model.rating))
                except ValueError:
                    continue

        if ratings:
            return sum(ratings) / len(ratings)
        else:
            return None

    def save(self, *args, **kwargs):
        self.average_rating = self.calculate_average_rating()

        # Check if all three judge fields are filled
        self.all_judges_filled = all([self.judge_model1, self.judge_model2, self.judge_model3])

        super().save(*args, **kwargs)

        # Count of non-none PDF fields
        pdf_fields = ['pdf_file1', 'pdf_file2', 'pdf_file3', 'pdf_file4', 'pdf_file5']
        non_none_pdf_count = sum(1 for field in pdf_fields if getattr(self, field, None))

        # Update related JudgeModel instances if they exist
        for judge_model in [self.judge_model1, self.judge_model2, self.judge_model3]:
            if judge_model:
                judge_model.submission = str(self.id)
                judge_model.sub_number = str(non_none_pdf_count)
                judge_model.save()  # Save the changes to the JudgeModel instance

    @property
    def non_empty_judge_fields_count(self):
        count = 0
        for judge_field in [self.judge_model1, self.judge_model2, self.judge_model3]:
            if judge_field is not None:
                count += 1
        return count

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
                "average_rating": self.average_rating,
                "all_judges_filled": self.all_judges_filled,
                "is_email_notified": self.is_email_notified,
                "is_active": self.is_active,
        }

    def __str__(self):
        return f"{str(self.firstname).capitalize()} {str(self.lastname).capitalize()}'s Submission"
    
    class Meta:
        verbose_name = "Student Submission"


class GeneralSettings(models.Model):
    key = models.CharField(max_length=255, unique=True, help_text="Unique name of the setting.")
    value = models.BooleanField(default=True, help_text="Value of the setting.")
    description = models.TextField(blank=True, help_text="Description of the setting.")

    def __str__(self):
        return f"{self.key}: {self.value}"
