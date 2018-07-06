import sys
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

#consider using Outlook REST API instead of storing passwords

#for storing passwords use:
#https://pypi.org/project/keyring/#description
#https://nakedsecurity.sophos.com/2013/11/20/serious-security-how-to-store-your-users-passwords-safely/
#https://pypi.org/project/bcrypt/
#http://dustwell.com/how-to-handle-passwords-bcrypt.html
#actually this:
#https://stackoverflow.com/questions/7014953/i-need-to-securely-store-a-username-and-password-in-python-what-are-my-options
#https://stackoverflow.com/questions/12042724/securely-storing-passwords-for-use-in-python-script
class Login(object):
    def login(self):
        try:
            server=smtplib.SMTP('smtp.office365.com',587)
            server.ehlo()
            context=ssl.create_default_context()
            server.starttls(context=context)
            server.login(self.e_user.get(),self.e_pass.get())
            server.quit()
            return 'SUCCESS'
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror('Error de autenticación','Error en usuario/contraseña.')
            return 'AUTH_ERROR'
        except Exception as err:
            tb=sys.exec_info()[2]
            messagebox.showerror('Error desconocido',tb+'\n'+err)
            return 'UNKN_ERROR'
