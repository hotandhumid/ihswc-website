
from django import forms

class CreateUserForm(forms.Form):
    firstname = forms.CharField(label="first name")
    lastname = forms.CharField(label="last name")
    email = forms.CharField(label="email")
    phone_number = forms.CharField(label="phone number")
    country = forms.CharField(label="country")
    city = forms.CharField(label="city")
    zipcode = forms.CharField(label="zipcode")
    grade_level = forms.CharField(label="grade level")
    birthday = forms.DateField(label="birthday", widget=forms.SelectDateWidget())
    school_name = forms.CharField(label="school name")
    school_address = forms.CharField(label="school address")
    pdf_id = forms.FileField(label="pdf id")
    parent_firstname = forms.CharField(label="parent first name")
    parent_lastname = forms.CharField(label="parent last name")
    parent_email = forms.CharField(label="parent email")
    parent_phone_number = forms.CharField(label="parent phone number")

    category1 = forms.CharField(label="category 1", widget=forms.Select(choices=[("dramatic script", "dramatic script"), ("critical essay", "critical essay"), ("poetry", "poetry"), ("flash fiction", "flash fiction"), ("shortstory", "shortstory")]))
    title1 = forms.CharField(label="title 1")
    word_count1 = forms.CharField(label="word count 1")
    pdf_file1 = forms.FileField(label="pdf file 1")

    category2 = forms.CharField(label="category 2", widget=forms.Select(choices=[("dramatic script", "dramatic script"), ("critical essay", "critical essay"), ("poetry", "poetry"), ("flash fiction", "flash fiction"), ("shortstory", "shortstory")]))
    title2 = forms.CharField(label="title 2")
    word_count2 = forms.CharField(label="word count 2")
    pdf_file2 = forms.FileField(label="pdf file 2")

    category3 = forms.CharField(label="category 3", widget=forms.Select(choices=[("dramatic script", "dramatic script"), ("critical essay", "critical essay"), ("poetry", "poetry"), ("flash fiction", "flash fiction"), ("shortstory", "shortstory")]))
    title3 = forms.CharField(label="title 3")
    word_count3 = forms.CharField(label="word count 3")
    pdf_file3 = forms.FileField(label="pdf file 3")

    category4 = forms.CharField(label="category 4", widget=forms.Select(choices=[("dramatic script", "dramatic script"), ("critical essay", "critical essay"), ("poetry", "poetry"), ("flash fiction", "flash fiction"), ("shortstory", "shortstory")]))
    title4 = forms.CharField(label="title 4")
    word_count4 = forms.CharField(label="word count 4")
    pdf_file4 = forms.FileField(label="pdf file 4")

    category5 = forms.CharField(label="category 5", widget=forms.Select(choices=[("dramatic script", "dramatic script"), ("critical essay", "critical essay"), ("poetry", "poetry"), ("flash fiction", "flash fiction"), ("shortstory", "shortstory")]))
    title5 = forms.CharField(label="title 5")
    word_count5 = forms.CharField(label="word count 5")
    pdf_file5 = forms.FileField(label="pdf file 5")


    student_checkbox = forms.BooleanField()
    teacher_checkbox = forms.BooleanField()

