import smtplib
import ssl
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import base64
#import easygui as gui
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def send_mail(subject,from_addr,to_addr,html_msg,att_filename=None):
    msg=MIMEMultipart()

    msg['Subject']=subject
    msg['From']=from_addr
    msg['To']=to_addr

    #html='<!DOCTYPE html><html><style>.underline{text-decoration:underline;}</style><body><h2 class="underline">Python mail</h2><p style="color:red">p1<br />p2</p></body></html>'
    html=html_msg
    body=MIMEText(html,'html')
    msg.attach(body)

    if att_filename:
        file=MIMEApplication(open(filename,'rb').read())
        file.add_header('Content-Disposition','attachment',filename=filename.split('/')[-1])
        msg.attach(file)

    server=smtplib.SMTP('smtp.office365.com',587)
    server.ehlo()
    context=ssl.create_default_context()
    server.starttls(context=context)
    server.login(USER,PASS)
    server.sendmail(msg['From'],msg['To'],msg.as_string())
    server.quit()

#when attach button pressed
def attach(self):
    self.filename=filedialog.askopenfilename()
    self.t_body.delete(1.0,tk.END)
    self.t_body.insert(tk.END,filename.split('/')[-1])

def login(window):
    try:
        server=smtplib.SMTP('smtp.office365.com',587)
        server.ehlo()
        server.starttls()
        server.login(window.e_user.get(),window.e_pass.get())
        server.quit()
        messagebox.showinfo('!','Success!')
        window.destroy()
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror('Error','Error en usuario/contraseña')
    except Exception as err:
        #messagebox.showerror('Error',err)
        tb = sys.exc_info()[2]
        raise err.with_traceback(tb)

def w_login():
    login_window=tk.Tk()

    login_window.l_user=tk.Label(login_window,text='User')
    login_window.l_pass=tk.Label(login_window,text='Pass')
    login_window.l_user.grid(row=0,column=0)
    login_window.l_pass.grid(row=0,column=1)

    login_window.e_user=tk.Entry(login_window,textvariable=login_window.v_user)
    login_window.e_pass=tk.Entry(login_window,textvariable=login_window.v_pass)
    login_window.e_user.grid(row=1,column=0)
    login_window.e_pass.grid(row=1,column=1)

    b_logmein=tk.Button(login_window,text='Log in',command=lambda x=login_window:login(x))
    b_logmein.grid(row=2,column=0,columnspan=2)

    login_window.mainloop()

window=tk.Tk()

window.b_login=tk.Button(window,text='Iniciar sesión',command=w_login)
window.b_attach=tk.Button(window,text='Adjuntar archivo',command=attach)
window.b_login.grid(row=0,column=0)
window.b_attach.grid(row=1,column=0)

window.t_body=tk.Text(window,height=6,width=60)
window.t_body.grid(row=2,column=0)

window.mainloop()
