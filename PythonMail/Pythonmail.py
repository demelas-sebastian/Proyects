import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import base64
import easygui as gui

msg=MIMEMultipart()

msg['Subject']='Some HTML mail'
msg['From']='sdemelas@scouts.org.ar'
msg['To']='sdemelas@scouts.org.ar'

html='<!DOCTYPE html><html><style>.underline{text-decoration:underline;}</style><body><h2 class="underline">Python mail test</h2><p style="color:red">p1<br />p2</p></body></html>'

body=MIMEText(html,'html')

msg.attach(body)

pdf=MIMEApplication(open(gui.fileopenbox('Your file:','Open'),'rb').read())

pdf.add_header('Content-Disposition', 'attachment', filename="Some PDF")

msg.attach(pdf)

server=smtplib.SMTP('smtp.office365.com',587)

server.ehlo()

server.starttls()

server.login('sdemelas@scouts.org.ar',base64.b64decode('MUYxaTJiM28=').decode('utf8'))

server.sendmail(msg['From'],msg['To'],msg.as_string())

server.quit()
