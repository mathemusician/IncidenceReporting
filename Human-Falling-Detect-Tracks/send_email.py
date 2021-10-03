import smtplib
from time import sleep
from email.mime.text import MIMEText


def send_message(text):
    sender = "Private Person <from@example.com>"
    receiver = "A Test User <to@example.com>"
    message = MIMEText(f"""
    Subject: Hi Mailtrap
    To: {receiver}
    From: {sender}
    Incident has been reported:
    {text}
    """)
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("49417da170b843", "bc7c773a91168e")
        A = server.sendmail(sender, receiver, message.as_string())


if __name__ == "__main__":
    send_message("message")
