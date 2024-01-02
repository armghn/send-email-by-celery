from django.urls import path
from .views import send_mail_to_all_users

urlpatterns = [
    path('sendmail/', send_mail_to_all_users,name="send_mail_to_all_users"),
]