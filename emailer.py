from email.message import EmailMessage
import ssl
import smtplib

def sendMail(theReceiver, body):
    emailSender = "automatieseepos@gmail.com"
    emailPassword = "sultyrrisvpqtony"
    emailReceiver = theReceiver
    subject = "Encoded files"
    body = body
    em = EmailMessage()
    em['From'] = emailSender
    em['To'] = emailReceiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, emailPassword)
        smtp.sendmail(emailSender, emailReceiver, em.as_string())
