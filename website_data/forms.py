
from django import forms
from datetime import date


class JudgeForm(forms.Form):
    graded_by = forms.CharField()
    review = forms.CharField(widget=forms.Textarea)
    # rating = forms.CharField(widget=forms.RadioSelect(choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"),("5", "5")]))
    rating = forms.CharField()
    submission = forms.CharField(widget=forms.HiddenInput())

class TestFileForm(forms.Form):
    firstname = forms.CharField(required=True, label="first name")
    lastname = forms.CharField(required=True, label="last name")
    email = forms.CharField(required=True, label="email")
    phone_number = forms.CharField(required=True, label="phone number")
    country = forms.CharField(required=True, label="country")
    city = forms.CharField(required=True, label="city")
    zipcode = forms.CharField(required=True, label="zipcode")
    grade_level = forms.CharField(required=True, label="grade level")
    birthday = forms.DateField(required=True, initial=date.today(),label="birthday", widget=forms.SelectDateWidget(years=range(1970, int(date.today().strftime("%Y")) + 1)))
    school_name = forms.CharField(required=True, label="school name")
    school_address = forms.CharField(required=True, label="school address")
    parent_firstname = forms.CharField(required=True, label="parent first name")
    parent_lastname = forms.CharField(required=True, label="parent last name")
    parent_email = forms.CharField(required=True, label="parent email")
    parent_phone_number = forms.CharField(required=True, label="parent phone number")

    category1 = forms.CharField(required=True, label="category 1", widget=forms.Select(choices=[("Dramatic Script", "Dramatic Script"), ("Critical Essay", "Critical Essay"), ("Poetry", "Poetry"), ("Flash Fiction", "Flash Fiction"), ("Shortstory", "Shortstory")]))
    title1 = forms.CharField(required=True, label="title 1")
    word_count1 = forms.CharField(required=True, label="word count 1")
    pdf_file1 = forms.FileField(widget=forms.ClearableFileInput(attrs={"accept": "application/pdf", "onchange": "getFileData(this)"}),required=True, label="pdf file 1")
    
    category2 = forms.CharField(required=False, label="category 2", widget=forms.Select(choices=[("Dramatic Script", "Dramatic Script"), ("Critical Essay", "Critical Essay"), ("Poetry", "Poetry"), ("Flash Fiction", "Flash Fiction"), ("Shortstory", "Shortstory")]))
    title2 = forms.CharField(required=False, label="title 2")
    word_count2 = forms.CharField(required=False, label="word count 2")
    pdf_file2 = forms.FileField(widget=forms.ClearableFileInput(attrs={"accept": "application/pdf", "onchange": "getFileData(this)"}),required=False, label="pdf file 2")

    category3 = forms.CharField(required=False, label="category 3", widget=forms.Select(choices=[("Dramatic Script", "Dramatic Script"), ("Critical Essay", "Critical Essay"), ("Poetry", "Poetry"), ("Flash Fiction", "Flash Fiction"), ("Shortstory", "Shortstory")]))
    title3 = forms.CharField(required=False, label="title 3")
    word_count3 = forms.CharField(required=False, label="word count 3")
    pdf_file3 = forms.FileField(widget=forms.ClearableFileInput(attrs={"accept": "application/pdf", "onchange": "getFileData(this)"}),required=False, label="pdf file 3")

    category4 = forms.CharField(required=False, label="category 4", widget=forms.Select(choices=[("Dramatic Script", "Dramatic Script"), ("Critical Essay", "Critical Essay"), ("Poetry", "Poetry"), ("Flash Fiction", "Flash Fiction"), ("Shortstory", "Shortstory")]))
    title4 = forms.CharField(required=False, label="title 4")
    word_count4 = forms.CharField(required=False, label="word count 4")
    pdf_file4 = forms.FileField(widget=forms.ClearableFileInput(attrs={"accept": "application/pdf", "onchange": "getFileData(this)"}),required=False, label="pdf file 4")

    category5 = forms.CharField(required=False, label="category 5", widget=forms.Select(choices=[("Dramatic Script", "Dramatic Script"), ("Critical Essay", "Critical Essay"), ("Poetry", "Poetry"), ("Flash Fiction", "Flash Fiction"), ("Shortstory", "Shortstory")]))
    title5 = forms.CharField(required=False, label="title 5")
    word_count5 = forms.CharField(required=False, label="word count 5")
    pdf_file5 = forms.FileField(widget=forms.ClearableFileInput(attrs={"accept": "application/pdf", "onchange": "getFileData(this)"}),required=False, label="pdf file 5")
