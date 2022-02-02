import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

class SendEmailUtility(object):

    def __init__(self):
        print ('send email utility')

    def send_mail_with_attachment(self,from_user,from_password,to,subject,text,attach):
        msg = MIMEMultipart()

        msg['From'] = from_user
        msg['To'] = to
        msg['Subject'] = subject

        msg.attach(MIMEText(text))

        part = MIMEBase('application','octet-stream')
        part.set_payload(open(attach,'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition','attachment; filename="%s"'%os.path.basename(attach))
        msg.attach(part)

        mailServer = smtplib.SMTP("smtp.gmail.com",587)

        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(from_user, from_password)
        mailServer.sendmail(from_user, to, msg.as_string())
        mailServer.close()

    def send_mail_no_attachment(self,from_user,from_password,to,subject,text):
        msg = MIMEMultipart()

        msg['From'] = from_user
        msg['To'] = to
        msg['Subject'] = subject

        msg.attach(MIMEText(text))

        mailServer = smtplib.SMTP("smtp.gmail.com",587)

        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(from_user, from_password)
        mailServer.sendmail(from_user, to, msg.as_string())
        mailServer.close()
