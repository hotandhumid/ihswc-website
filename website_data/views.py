from django.shortcuts import render, redirect
from .forms import CreateUserForm, TestFileForm
from .models import CreateUserModel, TestFileModel
# Create your views here.

def send_to_home(request):
    return redirect("/index")


def about(request):
    return render(request, "about.html")


def index(request):
    return render(request, "index.html")


def process(request):
    return render(request, "process.html")

def test(request):
    if request.method == "POST":

        form = TestFileForm(request.POST, request.FILES)

        if form.is_valid():
            print(request.FILES)
            f = TestFileModel(file=request.FILES['file'])
            f.save()
    else:
        form = TestFileForm()

    return render(request, "test.html", {"form": form})

def form(request):
    if request.method == "POST":

        form = CreateUserForm(request.POST, request.FILES)

        if form.is_valid():
            print(request.FILES)
            cd = form.cleaned_data

            f = CreateUserModel(
                firstname=cd["firstname"],
                lastname=cd["lastname"],
                email=cd["email"],
                phone_number=cd["phone_number"],
                country=cd["country"],
                city=cd["city"],
                zipcode=cd["zipcode"],
                grade_level=cd["grade_level"],
                birthday=cd["birthday"],
                school_name=cd["school_name"],
                school_address=cd["school_address"],
                pdf_id=request.FILES["pdf_id"],
                parent_firstname=cd["parent_firstname"],
                parent_lastname=cd["parent_lastname"],
                parent_email=cd["parent_email"],
                parent_phone_number=cd["parent_phone_number"],

                category1=cd["category1"],
                title1=cd["title1"],
                word_count1=cd["word_count1"],
                pdf_file1=request.FILES["pdf_file1"],

                category2=cd["category2"],
                title2=cd["title2"],
                word_count2=cd["word_count2"],
                pdf_file2=request.FILES["pdf_file2"],

                category3=cd["category3"],
                title3=cd["title3"],
                word_count3=cd["word_count3"],
                pdf_file3=request.FILES["pdf_file3"],

                category4=cd["category4"],
                title4=cd["title4"],
                word_count4=cd["word_count4"],
                pdf_file4=request.FILES["pdf_file4"],

                category5=cd["category5"],
                title5=cd["title5"],
                word_count5=cd["word_count5"],
                pdf_file5=request.FILES["pdf_file5"],
            )

            f.save()

            return redirect("/awards")
    else:
        form = CreateUserForm()

    return render(request, "form.html", {"form": form})


def rules(request):
    return render(request, "rules.html")


def awards(request):
    return render(request, "awards.html")


def submissions(request):
    return render(request, "submissions.html", {"submissions": list(CreateUserModel.objects.all().values())})
