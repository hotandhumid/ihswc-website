
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

    category1 = forms.CharField(label="category", widget=forms.Select(choices=["dramatic script", "critical essay", "poetry", "flash fiction", "shortstory"]))
    title1 = forms.CharField(label="title")
    word_count1 = forms.CharField(label="word count")
    pdf_file1 = forms.FileField(label="pdf file")

    category2 = forms.CharField(label="category", widget=forms.Select(choices=["dramatic script", "critical essay", "poetry", "flash fiction", "shortstory"]))
    title2 = forms.CharField(label="title")
    word_count2 = forms.CharField(label="word count")
    pdf_file2 = forms.FileField(label="pdf file")

    category3 = forms.CharField(label="category", widget=forms.Select(choices=["dramatic script", "critical essay", "poetry", "flash fiction", "shortstory"]))
    title3 = forms.CharField(label="title")
    word_count3 = forms.CharField(label="word count")
    pdf_file3 = forms.FileField(label="pdf file")

    category4 = forms.CharField(label="category", widget=forms.Select(choices=["dramatic script", "critical essay", "poetry", "flash fiction", "shortstory"]))
    title4 = forms.CharField(label="title")
    word_count4 = forms.CharField(label="word count")
    pdf_file4 = forms.FileField(label="pdf file")

    category5 = forms.CharField(label="category", widget=forms.Select(choices=["dramatic script", "critical essay", "poetry", "flash fiction", "shortstory"]))
    title5 = forms.CharField(label="title")
    word_count5 = forms.CharField(label="word count")
    pdf_file5 = forms.FileField(label="pdf file")


    student_checkbox = forms.BooleanField()
    teacher_checkbox = forms.BooleanField()

