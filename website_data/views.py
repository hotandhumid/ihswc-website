
from django.shortcuts import render, redirect

from .models import TestFileModel, JudgeModel1, JudgeModel2, JudgeModel3
from .forms import TestFileForm, JudgeForm1, JudgeForm2, JudgeForm3
# Create your views here.

import smtplib
import mailtrap as mt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import requests


def email_page(request):
    if request.method == "POST":
        try:
            if request.POST['test'] == 'on':
                message = MIMEMultipart()
                message["From"] = "highschoolwritingcontest.com <mailtrap@highschoolwritingcontest.com>"
                message["To"] = request.POST['email']
                message["Subject"] = request.POST['subject']
                html_content = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Email</title>    
                </head>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0; display: flex; align-items: center; justify-content: center; min-height: 100vh; background-color: #f8f9fa;">
                    <div style="background-color: #ffffff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); overflow: hidden; width: 80%; max-width: 600px; margin: 0 auto;">
                        <header style="background-color: #007BFF; color: #fff; padding: 10px; text-align: center;">
                            <h1>Mesage from highschoolwritingcontest!</h1>
                        </header>

                        <div style="background-color: #ffffff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); overflow: hidden; width: 80%; max-width: 600px; margin: 0 auto; padding: 20px;">
                            <div style="min-height: calc(100vh - 60px); box-sizing: border-box;">
                                <p>Hello,</p>

                                <p>{request.POST['message']}</p>

                                <p>Best regards,<br>
                                highschoolwritingcontest.com</p>
                            </div>
                        </div>

                        <footer style="background-color: #f4f4f4; padding: 10px; text-align: center;">
                            <p>Copyright © 2023. All rights reserved.</p>
                        </footer>
                    </div>
                </body>
                </html>
                """
                message.attach(MIMEText(html_content, "html"))

                with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
                    server.starttls()
                    server.login("api", "c76c34495d8006938a9177c6dff66489")
                    server.sendmail("mailtrap@highschoolwritingcontest.com", request.POST['email'], message.as_string())
        except:
            if request.POST['email'].upper() == "ALL":
                print("ALL")
                message = MIMEMultipart()
                message["From"] = "highschoolwritingcontest.com <mailtrap@highschoolwritingcontest.com>"
                recipients = [sub['email'] for sub in TestFileModel.objects.all().values()]
                message["To"] = "mailtrap@highschoolwritingcontest.com"
                message["Subject"] = request.POST['subject']
                html_content = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Email</title>    
                </head>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0; display: flex; align-items: center; justify-content: center; min-height: 100vh; background-color: #f8f9fa;">
                    <div style="background-color: #ffffff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); overflow: hidden; width: 80%; max-width: 600px; margin: 0 auto;">
                        <header style="background-color: #007BFF; color: #fff; padding: 10px; text-align: center;">
                            <h1>Message from highschoolwritingcontest!</h1>
                        </header>

                        <div style="background-color: #ffffff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); overflow: hidden; width: 80%; max-width: 600px; margin: 0 auto; padding: 20px;">
                            <div style="min-height: calc(100vh - 60px); box-sizing: border-box;">
                                <p>Hello,</p>

                                <p>{request.POST['message']}</p>

                                <p>Best regards,<br>
                                highschoolwritingcontest.com</p>
                            </div>
                        </div>

                        <footer style="background-color: #f4f4f4; padding: 10px; text-align: center;">
                            <p>Copyright © 2023. All rights reserved.</p>
                        </footer>
                    </div>
                </body>
                </html>
                """
                message.attach(MIMEText(html_content, "html"))

                with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
                    server.starttls()
                    server.login("api", "c76c34495d8006938a9177c6dff66489")
                    server.sendmail("mailtrap@highschoolwritingcontest.com", ["daniel.miami2005@gmail.com"] + recipients, message.as_string())
        
    return render(request, "email_page.html")


def submission(request):
    if request.method == "POST":
        if len(JudgeModel1.objects.filter(submission=request.GET['id'], sub_number=request.GET['sub'])) == 0:
            form1 = JudgeForm1(request.POST)
            if form1.is_valid():
                # if len(JudgeModel1.objects.filter(submission=request.GET['id'])) != 0:
                #     instance = JudgeModel1.objects.filter(submission=request.GET['id'])
                #     instance = instance[len(instance) - 1]
                #     f = JudgeModel1(graded_by=instance.graded_by, review=instance.review + " | " + form1.cleaned_data['review'], rating=instance.rating, submission=instance.submission)
                #     f.save()
                # else:
                cd = form1.cleaned_data
                f = JudgeModel1(graded_by=cd['graded_by'], review=cd['review'], rating=cd['rating'], submission=cd['submission'], sub_number=cd['sub_number'])
                f.save()
                return redirect("/admin-page?login=success&user=admin")
        if len(JudgeModel2.objects.filter(submission=request.GET['id'], sub_number=request.GET['sub'])) == 0:
            form2 = JudgeForm2(request.POST)
            if form2.is_valid():
                # if len(JudgeModel2.objects.filter(submission=request.GET['id'])) != 0:
                #     instance = JudgeModel2.objects.filter(submission=request.GET['id'])
                #     instance = instance[len(instance) - 1]
                #     f = JudgeModel2(graded_by=instance.graded_by, review=instance.review + " | " + form2.cleaned_data['review'], rating=instance.rating, submission=instance.submission)
                #     f.save()
                # else:
                cd = form2.cleaned_data
                f = JudgeModel2(graded_by=cd['graded_by'], review=cd['review'], rating=cd['rating'], submission=cd['submission'], sub_number=cd['sub_number'])
                f.save()
                return redirect("/admin-page?login=success&user=admin")
        if len(JudgeModel3.objects.filter(submission=request.GET['id'], sub_number=request.GET['sub'])) == 0:
            form3 = JudgeForm3(request.POST)
            if form3.is_valid():
                # if len(JudgeModel2.objects.filter(submission=request.GET['id'])) != 0:
                #     instance = JudgeModel2.objects.filter(submission=request.GET['id'])
                #     instance = instance[len(instance) - 1]
                #     f = JudgeModel2(graded_by=instance.graded_by, review=instance.review + " | " + form2.cleaned_data['review'], rating=instance.rating, submission=instance.submission)
                #     f.save()
                # else:
                cd = form3.cleaned_data
                f = JudgeModel3(graded_by=cd['graded_by'], review=cd['review'], rating=cd['rating'], submission=cd['submission'], sub_number=cd['sub_number'])
                f.save()
                return redirect("/admin-page?login=success&user=admin")
    else:
        form1 = JudgeForm1()
        form2 = JudgeForm2()
        form3 = JudgeForm3()

    sub = request.GET['sub']
    sub_dict = {
        "firstname": TestFileModel.objects.get(id=request.GET['id']).get_values()['firstname'],
        "lastname": TestFileModel.objects.get(id=request.GET['id']).get_values()['lastname'],
        "title": TestFileModel.objects.get(id=request.GET['id']).get_values()[f'title{sub}'],
        "category": TestFileModel.objects.get(id=request.GET['id']).get_values()[f'category{sub}'],
        "word_count": TestFileModel.objects.get(id=request.GET['id']).get_values()[f'word_count{sub}'],
        "pdf_file": TestFileModel.objects.get(id=request.GET['id']).get_values()[f'pdf_file{sub}'],
        "sub_number": sub,
    }

    if len(JudgeModel1.objects.filter(submission=request.GET['id'], sub_number=request.GET['sub'])) == 0:
        return render(request, "submission.html", {"submission": sub_dict, 
                                               "form": form1,
                                               "id": request.GET['id']})
    
    elif len(JudgeModel1.objects.filter(submission=request.GET['id'], sub_number=request.GET['sub'])) == 1 and len(JudgeModel2.objects.filter(submission=request.GET['id'], sub_number=request.GET['sub'])) == 0:
        return render(request, "submission.html", {"submission": sub_dict,
                                               "form": form2,
                                               "id": request.GET['id'],
                                                "judging1": JudgeModel1.objects.filter(submission=request.GET['id'])[len(JudgeModel1.objects.filter(submission=request.GET['id'])) - 1].get_values(),
                                                "judge_submitted": '1'
                                               })
    elif len(JudgeModel1.objects.filter(submission=request.GET['id'], sub_number=request.GET['sub'])) == 1 and len(JudgeModel2.objects.filter(submission=request.GET['id'], sub_number=request.GET['sub'])) == 1 and len(JudgeModel3.objects.filter(submission=request.GET['id'], sub_number=request.GET['sub'])) == 0:
        return render(request, "submission.html", {"submission": sub_dict,
                                               "form": form3,
                                               "id": request.GET['id'],
                                                "judging1": JudgeModel1.objects.filter(submission=request.GET['id'])[len(JudgeModel1.objects.filter(submission=request.GET['id'])) - 1].get_values(),
                                                "judging2": JudgeModel2.objects.filter(submission=request.GET['id'])[len(JudgeModel2.objects.filter(submission=request.GET['id'])) - 1].get_values(),
                                                "judge_submitted": '2'
                                               })
    elif len(JudgeModel1.objects.filter(submission=request.GET['id'], sub_number=request.GET['sub'])) == 1 and len(JudgeModel2.objects.filter(submission=request.GET['id'], sub_number=request.GET['sub'])) == 1 and len(JudgeModel3.objects.filter(submission=request.GET['id'], sub_number=request.GET['sub'])) == 1:
        return render(request, "submission.html", {"submission": sub_dict,
                                                   "judging1": JudgeModel1.objects.filter(submission=request.GET['id'])[len(JudgeModel1.objects.filter(submission=request.GET['id'])) - 1].get_values(),
                                                   "judging2": JudgeModel2.objects.filter(submission=request.GET['id'])[len(JudgeModel2.objects.filter(submission=request.GET['id'])) - 1].get_values(),
                                                   "judging3": JudgeModel3.objects.filter(submission=request.GET['id'])[len(JudgeModel3.objects.filter(submission=request.GET['id'])) - 1].get_values(),
                                                   "judge_submitted": '3'})

def admin_page(request):
    combined_model = list(JudgeModel1.objects.all().values()) + list(JudgeModel2.objects.all().values()) + list(JudgeModel3.objects.all().values())
    graded_lst = [int(i['submission']) for i in combined_model]
    countries = [d['country'] for d in list(TestFileModel.objects.all().values())]
    countries = set(countries)
    return render(request, "admin_page.html", {"submissions": list(TestFileModel.objects.all().values()),
                                               "gradings": combined_model,
                                               "graded_lst": graded_lst,
                                               "countries": countries})


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

            #~ EMAIL TO ME AND JACK
            # Set sender and recipient email addresses
            sender_name = "highschoolwritingcontest.com"
            sender_email = "mailtrap@highschoolwritingcontest.com"
            recipients = ["daniel.miami2005@gmail.com", "jack.jiaen.he@gmail.com"]
            # Create a MIME message
            message = MIMEMultipart()
            message["From"] = f"{sender_name} <{sender_email}>"
            message["To"] = ", ".join(recipients)
            message["Subject"] = f"New Submission | {cd['email']}: {cd['lastname']}, {cd['firstname']}"
            # Add the body to the HTML MIME message
            html_content = f"""
            <html>
                <head></head>
                <body>
                    <h1>{cd['firstname']} {cd['lastname']}</h1>
                    <p>Name: {cd['firstname']} {cd['lastname']}</p>
                    <p>Name: {cd['firstname']} {cd['lastname']}</p>
                    <p>Email: {cd['email']}</p>
                    <p>CONTACT INFO:</p>
                    <hr>
                    <p>Phone Number: {cd['phone_number']}</p>
                    <p>Country: {cd['country']}</p>
                    <p>City: {cd['city']}</p>
                    <p>Zipcode: {cd['zipcode']}</p>
                    <a href="https://highschoolwritingcontest.com/media/{files['pdf_file1']}">Write a review for 1</a>
                    <a href="https://highschoolwritingcontest.com/media/{files['pdf_file2']}">Write a review for 2</a>
                    <a href="https://highschoolwritingcontest.com/media/{files['pdf_file3']}">Write a review for 3</a>
                    <a href="https://highschoolwritingcontest.com/media/{files['pdf_file4']}">Write a review for 4</a>
                    <a href="https://highschoolwritingcontest.com/media/{files['pdf_file5']}">Write a review for 5</a>
                </body>
            </html>
            """
            message.attach(MIMEText(html_content, "html"))
            # Attach the PDF file
            pdf_url = "https://www.highschoolwritingcontest.com/media/ThebeautyofuncertaintyinlifebyhyeminKim_Nov.30.2023.pdf"
            pdf_response = requests.get(pdf_url)
            pdf_content = pdf_response.content
            pdf_attachment = MIMEApplication(pdf_content, _subtype="pdf")
            pdf_attachment.add_header("Content-Disposition", "attachment", filename="attachment.pdf")
            message.attach(pdf_attachment)
            with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
                server.starttls()
                server.login("api", "c76c34495d8006938a9177c6dff66489")
                server.sendmail(sender_email, recipients, message.as_string())


            #~ EMAIL TO SUBMITTER
            # Set sender and recipient email addresses
            sender_name = "highschoolwritingcontest.com"
            sender_email = "mailtrap@highschoolwritingcontest.com"
            # Create a MIME message
            message = MIMEMultipart()
            message["From"] = f"{sender_name} <{sender_email}>"
            message["To"] = cd['email']
            message["Subject"] = "Submission Success!"
            # Add the body to the HTML MIME message
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Email</title>    
            </head>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0; display: flex; align-items: center; justify-content: center; min-height: 100vh; background-color: #f8f9fa;">
                <div style="background-color: #ffffff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); overflow: hidden; width: 80%; max-width: 600px; margin: 0 auto;">
                    <header style="background-color: #007BFF; color: #fff; padding: 10px; text-align: center;">
                        <h1>Thank you for submitting, {cd['firstname']} {cd['lastname']}!</h1>
                    </header>

                    <div style="background-color: #ffffff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); overflow: hidden; width: 80%; max-width: 600px; margin: 0 auto; padding: 20px;">
                        <div style="min-height: calc(100vh - 60px); box-sizing: border-box;">
                            <p>Hello {cd['firstname']} {cd['lastname']},</p>

                            <p>Your submission has been received!</p>

                            <p>Donations of any amount are kindly appreciated! Donate <a href="https://writingwaves.org/checkout/donate?donatePageId=64836d536d69932109567eab">here</a> now!</p>

                            <p>Best regards,<br>
                            highschoolwritingcontest.com</p>
                        </div>
                    </div>

                    <footer style="background-color: #f4f4f4; padding: 10px; text-align: center;">
                        <p>Copyright © 2023. All rights reserved.</p>
                    </footer>
                </div>
            </body>
            </html>
            """
            message.attach(MIMEText(html_content, "html"))

            with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
                server.starttls()
                server.login("api", "c76c34495d8006938a9177c6dff66489")
                server.sendmail(sender_email, cd['email'], message.as_string())


            return redirect("/donate")
    else:
        form = TestFileForm()   
    
    model = TestFileModel.objects.all()
    emails = [i.email for i in model]
        
    return render(request, "form.html", {"form": form, "emails": emails})


def resubmit(request):
    if request.method == "POST":
        emails = [sub['email'] for sub in TestFileModel.objects.all().values()]
        if request.POST['resubmit_email'] in emails:
            return redirect(f"/resubmit_form?email={request.POST['resubmit_email']}")
    return render(request, "resubmit.html")


def resubmit_form(request):
    email = request.GET['email']
    initial_dict = TestFileModel.objects.filter(email=email)[0].get_values()

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
        form = TestFileForm(initial=initial_dict)

    print(form)

    return render(request, "resubmit_form.html", {"form": form})


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