from django.core.mail import EmailMessage
from .email_builder import EmailBuilder


class EmailService:
    @staticmethod
    def send(msg,user):
        text = EmailBuilder.content(user)
        email = EmailMessage(msg.subject, text, msg.frm, msg.to)
        email.content_subtype = "html"
        try:
            res = email.send()
        except Exception as e:
            res = e
        return res
