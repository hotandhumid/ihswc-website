from django.test import TestCase

# Create your tests here.

import mailtrap as mt

mail = mt.Mail(
    sender="mailtrap@highschoolwritingcontest.com",
    to=[mt.Address(email="daniel.miami2005@gmail.com"), mt.Address(email="jack.jiaen.he@gmail.com")],
    subject=f"highschoolwritingcontest.com | NEW SUBMISSION | ['email']",
    text=f"'firstname'], cd['lastname'] just submitted. Email: 'email']",
    category="Integration Test"
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