
from django import forms
from datetime import date


class TestFileForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={"onchange": "getFileData(this)"}),)

    
class CreateUserForm(forms.Form):
    firstname = forms.CharField(required=False, label="first name")
    lastname = forms.CharField(required=False, label="last name")
    email = forms.CharField(required=False, label="email")
    phone_number = forms.CharField(required=False, label="phone number")
    country = forms.CharField(required=False, label="country")
    city = forms.CharField(required=False, label="city")
    zipcode = forms.CharField(required=False, label="zipcode")
    grade_level = forms.CharField(required=False, label="grade level")
    birthday = forms.DateField(required=False, initial=date.today(),label="birthday", widget=forms.SelectDateWidget(years=range(1970, int(date.today().strftime("%Y")) + 1)))
    school_name = forms.CharField(required=False, label="school name")
    school_address = forms.CharField(required=False, label="school address")
    pdf_id = forms.FileField(widget=forms.ClearableFileInput(attrs={"onchange": "getFileData(this)"}),required=False, label="pdf id")
    parent_firstname = forms.CharField(required=False, label="parent first name")
    parent_lastname = forms.CharField(required=False, label="parent last name")
    parent_email = forms.CharField(required=False, label="parent email")
    parent_phone_number = forms.CharField(required=False, label="parent phone number")

    category1 = forms.CharField(required=False, label="category 1", widget=forms.Select(choices=[("dramatic script", "dramatic script"), ("critical essay", "critical essay"), ("poetry", "poetry"), ("flash fiction", "flash fiction"), ("shortstory", "shortstory")]))
    title1 = forms.CharField(required=False, label="title 1")
    word_count1 = forms.CharField(required=False, label="word count 1")
    pdf_file1 = forms.FileField(widget=forms.ClearableFileInput(attrs={"onchange": "getFileData(this)"}),required=False, label="pdf file 1")

    category2 = forms.CharField(required=False, label="category 2", widget=forms.Select(choices=[("dramatic script", "dramatic script"), ("critical essay", "critical essay"), ("poetry", "poetry"), ("flash fiction", "flash fiction"), ("shortstory", "shortstory")]))
    title2 = forms.CharField(required=False, label="title 2")
    word_count2 = forms.CharField(required=False, label="word count 2")
    pdf_file2 = forms.FileField(widget=forms.ClearableFileInput(attrs={"onchange": "getFileData(this)"}),required=False, label="pdf file 2")

    category3 = forms.CharField(required=False, label="category 3", widget=forms.Select(choices=[("dramatic script", "dramatic script"), ("critical essay", "critical essay"), ("poetry", "poetry"), ("flash fiction", "flash fiction"), ("shortstory", "shortstory")]))
    title3 = forms.CharField(required=False, label="title 3")
    word_count3 = forms.CharField(required=False, label="word count 3")
    pdf_file3 = forms.FileField(widget=forms.ClearableFileInput(attrs={"onchange": "getFileData(this)"}),required=False, label="pdf file 3")

    category4 = forms.CharField(required=False, label="category 4", widget=forms.Select(choices=[("dramatic script", "dramatic script"), ("critical essay", "critical essay"), ("poetry", "poetry"), ("flash fiction", "flash fiction"), ("shortstory", "shortstory")]))
    title4 = forms.CharField(required=False, label="title 4")
    word_count4 = forms.CharField(required=False, label="word count 4")
    pdf_file4 = forms.FileField(widget=forms.ClearableFileInput(attrs={"onchange": "getFileData(this)"}),required=False, label="pdf file 4")

    category5 = forms.CharField(required=False, label="category 5", widget=forms.Select(choices=[("dramatic script", "dramatic script"), ("critical essay", "critical essay"), ("poetry", "poetry"), ("flash fiction", "flash fiction"), ("shortstory", "shortstory")]))
    title5 = forms.CharField(required=False, label="title 5")
    word_count5 = forms.CharField(required=False, label="word count 5")
    pdf_file5 = forms.FileField(widget=forms.ClearableFileInput(attrs={"onchange": "getFileData(this)"}),required=False, label="pdf file 5")


