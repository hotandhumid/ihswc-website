
from django.shortcuts import render, redirect
from .models import TestFileModel, JudgeModel
from .forms import TestFileForm, JudgeForm
# Create your views here.

from django.core.mail import send_mail
import mailtrap as mt

def submission(request):
    if request.method == "POST":
        form = JudgeForm(request.POST)
        if form.is_valid():
            if len(JudgeModel.objects.filter(submission=request.GET['id'])) != 0:
                print('yes')
                instance = JudgeModel.objects.filter(submission=request.GET['id'])
                instance = instance[len(instance) - 1]
                f = JudgeModel(graded_by=instance.graded_by, review=instance.review + " | " + form.cleaned_data['review'], rating=instance.rating, submission=instance.submission)
                f.save()
            else:
                print('nooo')
                print(request.POST)
                cd = form.cleaned_data
                f = JudgeModel(graded_by=cd['graded_by'], review=cd['review'], rating=cd['rating'], submission=cd['submission'])
                f.save()
        else:
            print(request.POST)
            print(form.errors)

    else:
        form = JudgeForm()

    if len(JudgeModel.objects.filter(submission=request.GET['id'])) == 0:
        return render(request, "submission.html", {"submission": TestFileModel.objects.get(id=request.GET['id']).get_values(), 
                                               "form": form,
                                               "id": request.GET['id']})
    else:
        return render(request, "submission.html", {"submission": TestFileModel.objects.get(id=request.GET['id']).get_values(),
                                                   "judging": JudgeModel.objects.filter(submission=request.GET['id'])[len(JudgeModel.objects.filter(submission=request.GET['id'])) - 1].get_values(),
                                                   "judge_submitted": True})

def admin_page(request):
    graded_lst = [int(i['submission']) for i in JudgeModel.objects.all().values()]
    return render(request, "admin_page.html", {"submissions": list(TestFileModel.objects.all().values()),
                                               "gradings": list(JudgeModel.objects.all().values()),
                                               "graded_lst": graded_lst})


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


            # send_mail(
            #     f"highschoolwritingcontest.com | NEW SUBMISSION | {cd['email']}",
            #     f"{cd['firstname'], cd['lastname']} just submitted. Email: {cd['email']}",
            #     "mailtrap@highschoolwritingcontest.com",
            #     ["daniel.miami2005@gmail.com", "jack.jiaen.he@gmail.com"],
            #     fail_silently=False,
            # )
            import mailtrap as mt

            mail = mt.Mail(
                sender=mt.Address(email="mailtrap@highschoolwritingcontest.com", name="highschoolwritingcontest.com (my lovely email bot)"),
                to=[mt.Address(email="daniel.miami2005@gmail.com"), mt.Address(email="jack.jiaen.he@gmail.com")],
                subject=f"IHSWC Alert | New Submission by: {cd['email']}",
                text=f"\nName: {cd['firstname']} {cd['lastname']}.\nEmail: {cd['email']}\n\nCONTACT INFO:\n-------------------------------\nPhone Number: {cd['phone_number']}\nCountry: {cd['country']}\nCity: {cd['city']}\nZipcode: {cd['zipcode']}\n\nCheck it out: https://highschoolwritingcontest.com/media/{files['pdf_file1']}",
                category="Integration Test",
            )

            client = mt.MailtrapClient(token="c76c34495d8006938a9177c6dff66489")
            client.send(mail)

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