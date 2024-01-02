from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_email


def send_mail_to_all_users(request):
    send_email.delay()
    return HttpResponse("Email has been Sent Successfully")