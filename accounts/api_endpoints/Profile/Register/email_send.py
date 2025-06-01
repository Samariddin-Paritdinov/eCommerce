from django.core.mail import EmailMessage

def send_normal_email(data):
    try:
        email = EmailMessage(
            subject=data["email_subject"],
            body=data["email_body"],
            to=[data["to_email"]],
        )
        email.send(fail_silently=False)
    except Exception as e:
        print(f"Failed to send email to {data['to_email']}: {e}")