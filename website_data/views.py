from django.shortcuts import render, redirect
from .models import TestFileModel
from .forms import TestFileForm
# Create your views here.


def admin_page(request):
    return render(request, "admin_page.html", {"submissions": list(TestFileModel.objects.all().values())})


def sign_in(request):
    return render(request, "sign_in.html")


def send_to_home(request):
    return redirect("/home")


def about(request):
    return render(request, "about.html")


def home(request):
    return render(request, "home.html")


def process(request):
    return render(request, "process.html")

def test(request):
    if request.method == "POST":

        form = TestFileForm(request.POST, request.FILES)

        if form.is_valid():
            cd = form.cleaned_data
            
            raw_files = dict(request.FILES)
            files = {}
            file_names = ["pdf_file1", "pdf_file2", "pdf_file3", "pdf_file4", "pdf_file5"]
            
            for f in file_names:
                if f in raw_files.keys():
                    files.update({f : request.FILES[f] })
                else:
                    files.update({ f : "___" })

            f = TestFileModel(
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
                parent_firstname=cd["parent_firstname"],
                parent_lastname=cd["parent_lastname"],
                parent_email=cd["parent_email"],
                parent_phone_number=cd["parent_phone_number"],

                category1=cd["category1"],
                title1=cd["title1"],
                word_count1=cd["word_count1"],
                pdf_file1=files["pdf_file1"],

                category2=cd["category2"],
                title2=cd["title2"],
                word_count2=cd["word_count2"],
                pdf_file2=files["pdf_file2"],
            )
            f.save()
    else:
        form = TestFileForm()

    return render(request, "test.html", {"form": form})


def submit(request):
    return render(request, "submit.html")


def form(request):
    if request.method == "POST":

        form = TestFileForm(request.POST, request.FILES)

        if form.is_valid():
            cd = form.cleaned_data

            raw_files = dict(request.FILES)
            files = {}
            file_names = ["pdf_file1", "pdf_file2", "pdf_file3", "pdf_file4", "pdf_file5"]
            
            for f in file_names:
                if f in raw_files.keys():
                    files.update({f : request.FILES[f] })
                else:
                    files.update({ f : "___" })

            f = TestFileModel(
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
                parent_firstname=cd["parent_firstname"],
                parent_lastname=cd["parent_lastname"],
                parent_email=cd["parent_email"],
                parent_phone_number=cd["parent_phone_number"],

                category1=cd["category1"],
                title1=cd["title1"],
                word_count1=cd["word_count1"],
                pdf_file1=files["pdf_file1"],

                category2=cd["category2"],
                title2=cd["title2"],
                word_count2=cd["word_count2"],
                pdf_file2=files["pdf_file2"],

                category3=cd["category3"],
                title3=cd["title3"],
                word_count3=cd["word_count3"],
                pdf_file3=files["pdf_file3"],

                category4=cd["category4"],
                title4=cd["title4"],
                word_count4=cd["word_count4"],
                pdf_file4=files["pdf_file4"],

                category5=cd["category5"],
                title5=cd["title5"],
                word_count5=cd["word_count5"],
                pdf_file5=files["pdf_file5"],
            )

            f.save()

            return redirect("/donate")
    else:
        form = TestFileForm()   
    
    model = TestFileModel.objects.all()
    emails = [i.email for i in model]
        
    return render(request, "form.html", {"form": form, "emails": emails})


def rules(request):
    return render(request, "rules.html")


def awards(request):
    return render(request, "awards.html")


def submissions(request):
    return render(request, "submissions.html", {"submissions": list(TestFileModel.objects.all().values())})


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def donate(request):
    return render(request, "donate.html")