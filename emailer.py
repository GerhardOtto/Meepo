from email.message import EmailMessage
import ssl
import smtplib

# This function sends an email with the encoded file as an attachment
def sendMail(theReceiver, filePath):
    emailSender = "automatieseepos@gmail.com"
    emailPassword = "sultyrrisvpqtony"
    emailReceiver = theReceiver
    subject = "Encoded files"
    em = EmailMessage()
    em['From'] = emailSender
    em['To'] = emailReceiver
    em['Subject'] = subject

    with open(filePath, 'rb') as file:
        fileData = file.read()

    em.add_attachment(fileData, maintype='application', subtype='octet-stream', filename=filePath)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, emailPassword)
        smtp.sendmail(emailSender, emailReceiver, em.as_string())