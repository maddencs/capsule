from django.db import models


class GetStartedForm(models.Model):
    studio_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=30)
    current_website_status = models.CharField(max_length=250, blank=True, null=True)
    almost_there_question = models.CharField(max_length=250, blank=True, null=True)
    need_redesign = models.NullBooleanField()
    lets_do_it = models.NullBooleanField()
    other = models.CharField(max_length=250, blank=True, null=True)
    reach_me = models.CharField(max_length=50, blank=True, null=True)
    more_info = models.NullBooleanField()
    current_website = models.URLField(blank=True, null=True)
    other_questions = models.CharField(max_length=250, blank=True, null=True)
    please_send_me_information = models.NullBooleanField()
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    secondary_contact_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    secondary_email = models.EmailField(max_length=250, blank=True, null=True)
    secondary_phone_number = models.CharField(max_length=250, blank=True, null=True)
