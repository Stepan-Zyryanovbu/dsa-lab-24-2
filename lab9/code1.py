def send_email(to, subject, body):
    print(f"Connecting to SMTP server...")
    print(f"Sending email to {to} with subject '{subject}'...")
    print("Email sent.")


def send_sms(to, message):
    print(f"Connecting to SMS gateway...")
    print(f"Sending SMS to {to} with message '{message}'...")
    print("SMS sent.")

#первый код до и после рефакторинга (сверху до, снизу после)

def send(service, to, text):
    print(f"Connecting to {service}...")
    print(f"Sending message to {to} '{text}'...")
    print("Message sent.")


def send_email(to, subject, body):
    send("SMTP server", to, f"{subject}: {body}")


def send_sms(to, message):
    send("SMS gateway", to, message)
