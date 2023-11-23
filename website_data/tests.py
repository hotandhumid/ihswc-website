from django.test import TestCase

# Create your tests here.


import mailtrap as mt

mail = mt.Mail(
    sender=mt.Address(email="mailtrap@highschoolwritingcontest.com", name="Highschoolwritingcontest.com"),
    to=[mt.Address(email="daniel.miami2005@gmail.com"), mt.Address(email="jack.jiaen.he@gmail.com")],
    subject="IHSWC Alert | New Submission by: {cd['email']}",
    text="Name: {cd['firstname']} {cd['lastname']}.\n\nEmail: {cd['email']}\n\nCONTACT INFO:\n\nAddress: {cd['address']}\nPhone Number: {cd['phone_number']}\nCountry: {cd['country']}\nCity: {cd['city']}\n\nCheck it out: https://highschoolwritingcontest.com/admin-page/?login=success&user=admin",
    category="Integration Test",
)

client = mt.MailtrapClient(token="c76c34495d8006938a9177c6dff66489")
client.send(mail)
# PGPASSWORD=Weyd4ife877vMKgLpX4zJsDcbMHFgI6a psql -h dpg-cijna3p8g3nc2gamv6d0-a.oregon-postgres.render.com -U highschoolwritingcontest_user highschoolwritingcontest

# put nav in bar, make it sticky
# put logo on header
# make solid color background
# gray bar for nav
# make it look like duke
# get headshot for kai, testimony,
# add bar, with stats (140+ entries), 17+ awards given, 5 different countries