from django.test import TestCase

# Create your tests here.
# PGPASSWORD=Weyd4ife877vMKgLpX4zJsDcbMHFgI6a psql -h dpg-cijna3p8g3nc2gamv6d0-a.oregon-postgres.render.com -U highschoolwritingcontest_user highschoolwritingcontest


import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import requests


cd = {
    "email": "daniel.miami2005@gmail.com",
    "firstname": "Daniel",
    "lastname": "Li"
}

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