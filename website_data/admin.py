from django.contrib import admin
from .models import TestFileModel, JudgeModel1, JudgeModel2, JudgeModel3, GeneralSettings
import smtplib
import mailtrap as mt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
from django.http import HttpResponse
from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _


class NullFilterSpec(admin.SimpleListFilter):
    title = _('average rating')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'average_rating'

    def lookups(self, request, model_admin):
        return (
            ('None', _('No Grade')),
            ('notNone', _('Has Grade')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'None':
            return queryset.filter(average_rating__isnull=True)
        if self.value() == 'notNone':
            return queryset.filter(average_rating__isnull=False)


def create_award_action(award_value, award_name):
    def set_award(modeladmin, request, queryset):
        queryset.update(award=award_value)
    set_award.__name__ = f'set_award_{award_value}'
    set_award.short_description = f'Set award to {award_name}'
    return set_award


# Dynamically generate one action for each award option
for award_value, award_name in TestFileModel.AWARD_CATEGORIES:
    action = create_award_action(award_value, award_name)
    globals()[action.__name__] = action


def activate_testfiles(modeladmin, request, queryset):
    queryset.update(is_active=True)


def deactivate_testfiles(modeladmin, request, queryset):
    queryset.update(is_active=False)


def send_award_notification(modeladmin, request, queryset):
    total_submissions = TestFileModel.objects.filter(is_active=True).count() * 4

    def send_email(item):
        has_award = item.award and item.award != 'no_award'
        message = MIMEMultipart()
        message["From"] = "highschoolwritingcontest.com <mailtrap@highschoolwritingcontest.com>"
        message["To"] = item.email
        message["Subject"] = f'Congratulations on Your {item.get_award_display()} Award' if has_award else 'Thank You for Your Submission'

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
        
                        <p>Thank you for participating in Writing Contest and submitting your work. We appreciate the time, effort, and passion you invested in your submission. This year, we received an extraordinary number of entries, totaling {total_submissions}, each demonstrating remarkable talent and creativity</p>
        
                        <p>While we were unable to grant an award to every participant, we want to express our sincere gratitude for your contribution and encourage you to continue pursuing your passion and excellence in your work.</p>
                        <p>We look forward to the possibility of seeing your submissions in future events and wish you the best in your ongoing endeavors.</p>
                        
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
        if has_award:
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
            
                            <p>Congratulations on receiving the {item.get_award_display()} for your submission. Your work truly stood out among {total_submissions} submissions, showcasing exceptional talent and dedication.</p>
            
                            <p>We celebrate your success and look forward to seeing more of your contributions to the field.</p>
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
            server.sendmail("mailtrap@highschoolwritingcontest.com", item.email, message.as_string())

    for item in queryset:
        send_email(item)
        item.is_email_notified = True
        item.save()


def export_to_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]
    pdf_base_url = "https://www.highschoolwritingcontest.com/media/"
    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    response = HttpResponse(content_type='text/csv')
    # Append the current date to the filename
    response['Content-Disposition'] = f'attachment; filename="{meta}_{current_date}.csv"'
    writer = csv.writer(response)

    writer.writerow(field_names)  # Write the header row
    for obj in queryset:
        row = []
        for field in field_names:
            value = getattr(obj, field)
            # Check if the field is a FileField and specifically for PDF files
            if isinstance(obj._meta.get_field(field), models.FileField):
                value = pdf_base_url + value.name if value else ''  # Prepend the base URL to the file name, ensure there's a value
            row.append(value)
        writer.writerow(row)

    return response


export_to_csv.short_description = "Export selected rows to CSV"
activate_testfiles.short_description = "Activate selected items"
deactivate_testfiles.short_description = "Deactivate selected items"
send_award_notification.short_description = "Send award notification emails"


class TestFileModelAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'country', 'grade_level', 'average_rating', 'non_empty_judge_fields_count',
                    'all_judges_filled', 'award', 'is_email_notified', 'is_active')  # Customize as needed
    list_filter = ('all_judges_filled', 'award', 'is_email_notified', 'is_active', NullFilterSpec)  # Add your filters here
    search_fields = ('firstname', 'lastname', 'email')  # Customize search fields as needed
    ordering = ('-average_rating',)  # Sort by average rating in descending order
    actions = [globals()[f'set_award_{award_value}'] for award_value, _ in TestFileModel.AWARD_CATEGORIES] + [activate_testfiles, deactivate_testfiles, send_award_notification, export_to_csv]

    def non_empty_judge_fields_count(self, obj):
        return obj.non_empty_judge_fields_count

    non_empty_judge_fields_count.short_description = 'Judge Count'  # 自定义列的标题


admin.site.register(TestFileModel, TestFileModelAdmin)
admin.site.register(JudgeModel1)
admin.site.register(JudgeModel2)
admin.site.register(JudgeModel3)
admin.site.register(GeneralSettings)
