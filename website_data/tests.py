from django.test import TestCase

# Create your tests here.


import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Set your Mailtrap credentials
mailtrap_username = "your_mailtrap_username"
mailtrap_password = "your_mailtrap_password"

# Set sender and recipient email addresses
sender_email = "mailtrap@highschoolwritingcontest.com"
recipients = ["daniel.miami2005@gmail.com", "jack.jiaen.he@gmail.com"]

# Create a MIME message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(recipients)
message["Subject"] = "Test Email Subject"

# Add the body to the MIME message
html_content = "This is a test email with an attached PDF file."
message.attach(MIMEText(html_content, "html"))

# Attach the PDF file
pdf_file_path = "/Users/dl/Documents/html_css_js_projects/websites/djangos/jacks-website/media/Read_and_Respond__dOnYPDl.pdf"
with open(pdf_file_path, "rb") as pdf_file:
    pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
    pdf_attachment.add_header("Content-Disposition", f"attachment; filename={pdf_file_path}")
    message.attach(pdf_attachment)


with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
    server.starttls()
    server.login("api", "c76c34495d8006938a9177c6dff66489")
    server.sendmail("highschoolwritingcontest.com <mailtrap@highschoolwritingcontest.com>", recipients, message.as_string())


# PGPASSWORD=Weyd4ife877vMKgLpX4zJsDcbMHFgI6a psql -h dpg-cijna3p8g3nc2gamv6d0-a.oregon-postgres.render.com -U highschoolwritingcontest_user highschoolwritingcontest

# put nav in bar, make it sticky
# put logo on header
# make solid color background
# gray bar for nav
# make it look like duke
# get headshot for kai, testimony,
# add bar, with stats (140+ entries), 17+ awards given, 5 different countries