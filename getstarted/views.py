from django.shortcuts import render
from .models import GetStartedForm
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
from django.views.decorators.csrf import csrf_exempt
from .config import CAPSULE_URL, API_AUTH
import requests


def render_xml(request, template_name, data):
    return render(request, template_name, context={'data': data})

def send_mail(data):
    subject = "Let\'s Get Started! - " + data.studio_name
    message = {}
    for key in data.__dict__.keys():
        if data.__dict__[key]:
            message[key] = data.__dict__[key]
    from_email = 'maddencs@gmail.com'
    to_email = 'csmadden@gmail.com'
    body = render_to_string('email.html', {'form': message})
    email = EmailMessage(subject, body, from_email, to=[to_email])
    email.content_subtype = 'html'
    email.send()
    return None


def capsule_add_organisation(request, data):
    """send xml request to capsule crm"""
    r = requests.post(CAPSULE_URL + '/api/organisation', headers={'Content-Type': 'application/xml'}, auth=API_AUTH, data=render_xml(request, 'organisation.xml', data))
    """
    Now we have to split the url along the /'s and get the last item
    then send that to the capsule API to add the tag to the organisation
    """
    org_id = r.headers['location'].split('/')
    org_id = org_id[len(org_id)-1]
    tag_r = requests.post(CAPSULE_URL + '/api/party/' + org_id + '/tag/Prospect', auth=API_AUTH)
    send_mail(data)

@csrf_exempt
def new_request(request):
    """receive request from form, create/send email to stacey
    send post request to capsule api to create organization and
    opportunity"""
    if request.method == 'POST':
        data = request.POST
        form = GetStartedForm.objects.create(studio_name=data['Studio_Name'],
                        phone_number=data['Phone_Number'],
                        current_website_status=data['Current_website_status'],
                        almost_there_question=data['Almost_there_question'],
                        need_redesign=data['Need_redesign'],
                        lets_do_it=data['Lets_DO_IT'],
                        reach_me=data['Reach_me'],
                        current_website=data['My_domain_name_is'],
                        other_questions=data['Other_questions'],
                        please_send_me_information=data['Please_send_me_information'],
                        contact_name=data['Contact_Name'],
                        email=data['email'],
                        secondary_email=data['Secondary_email'],
                        secondary_contact_name=data['Secondary_Contact_Name'],
                        secondary_phone_number=data['Secondary_Phone_Number'])
        capsule_add_organisation(request, form)
    else:
        pass
    return render(request, 'form.html')
