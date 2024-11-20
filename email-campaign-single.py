import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
  sender_email = "ayushsk.dev@gmail.com"
  sender_password = "ugxt gbtc czge cxsb"

  message = MIMEText(body)
  message["Subject"] = subject
  message["From"] = sender_email
  message["To"] = to_email

  with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to_email, message.as_string())

send_email("Hello", "This is a test email", "pryoshock729@gmail.com")