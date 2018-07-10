import sys,os,traceback
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import keyring

#consider using Outlook REST API instead of storing passwords
#using keyring for pass storage... for now

#maybe change this to a hash generated at runtime?
USER_RECOVER_KEY='magical_user_recovering_key'

class Login():
    def login(self):
        self.e_user.config(state=tk.DISABLED)
        self.e_pass.config(state=tk.DISABLED)
        exc_info=[]
        try:
            server=smtplib.SMTP('smtp.office365.com',587)
            server.ehlo()
            context=ssl.create_default_context()
            server.starttls(context=context)
            server.login(self.e_user.get(),self.e_pass.get())
            keyring.set_password(self.service_name,self.e_user.get(),self.e_pass.get())
            keyring.set_password(self.service_name,USER_RECOVER_KEY,self.e_user.get())
            server.quit()
            return ('SUCCESS',0,0)
        except smtplib.SMTPAuthenticationError:
            exc_info=[i for i in sys.exc_info()]
            exc_info.append('AUTH_ERROR')
        except keyring.errors.PasswordSetError:
            exc_info=[i for i in sys.exc_info()]
            exc_info.append('CRYPT_ERROR')
        except Exception:
            exc_info=[i for i in sys.exc_info()]
            exc_info.append('UNKN_ERROR')
        finally:
            self.e_user.config(state=tk.NORMAL)
            self.e_pass.config(state=tk.NORMAL)
            if not exc_info==[]:
                error_instance=exc_info[1].__repr__()
                traceback.print_tb(exc_info[2],file=open('trace.txt','w+'))
                trace=open('trace.txt').read()
                os.remove('trace.txt')
                error=exc_info[3]
                exc_info=[]
                return (error,error_instance,trace)

    def logout(self):
        exc_info=[]
        try:
            user=keyring.get_password(self.service_name,USER_RECOVER_KEY)
            keyring.delete_password(self.service_name,user)
            keyring.delete_password(self.service_name,USER_RECOVER_KEY)
            return ('SUCCESS',0,0)
        except keyring.errors.PasswordDeleteError:
            exc_info=[i for i in sys.exc_info()]
            exc_info.append('PSDEL_ERROR')
        except Exception:
            exc_info=[i for i in sys.exc_info()]
            exc_info.append('UNKN_ERROR')
        finally:
            if not exc_info==[]:
                error_instance=exc_info[1].__repr__()
                traceback.print_tb(exc_info[2],file=open('trace.txt','w+'))
                trace=open('trace.txt').read()
                os.remove('trace.txt')
                error=exc_info[3]
                exc_info=[]
                return (error,error_instance,trace)

class Mail(object):
    def __init__(self,window,parent,subject=None,to=None,_from=None,msg=None):
        self.window=window
        self.parent=parent
        self.msg=MIMEMultipart()
        if not subject==None:
            self.msg['Subject']=subject
        if not to==None:
            self.msg['To']=to
        if not _from==None:
            self.msg['From']=_from
        if not msg==None:
            self.body=MIMEText(msg,'html')
            self.msg.attach(self.body)

    def attach_file(self,filenames):
        self.filenames=filenames
        for i in self.filenames:
            file=MIMEApplication(open(i,'rb').read())
            file.add_header('Content-Disposition','attachment',filename=i.split('/')[-1])
            self.msg.attach(file)

    def send_mail(self):
        self.msg['Subject']=self.parent.e_subject.get()
        self.msg['To']=self.parent.e_to.get()
        self.msg['From']=self.parent.this_address+'no address'#remove for production
        self.msg['CC']=self.parent.e_cc.get()
        self.body=MIMEText(self.parent.t_body.get(1.0,tk.END),'html')
        self.msg.attach(self.body)
        print(self.msg.items())
        """
        try:
            self.connect()
            #send mail here
        except:
            pass
            #shit happens
        finally:
            try:
                self.server.quit()
            except:
                #whatever idc
                pass
"""
    def connect(self):
        self.server=smtplib.SMTP('smtp.office365.com',587)
        self.server.ehlo()
        self.server.starttls(context=ssl.create_default_context())
        self.server.login(
            keyring.get_password(self.parent.service_name,USER_RECOVER_KEY),
            keyring.get_password(self.parent.service_name,
                keyring.get_password(self.parent.service_name,USER_RECOVER_KEY)))

class Params():
    def search_params(self):
        i=-1
        text=self.parent.t_body.get(1.0,tk.END)
        params_index_beg=[]
        params_index_end=[]
        cycle=0
        error=False
        while True:
            next_beg=text.find('<<',i+1)
            if not next_beg==-1:
                params_index_beg.append(next_beg)
                i=next_beg
            else:
                break
        i=-1
        while True:
            next_end=text.find('>>',i+1)
            if not next_end==-1:
                params_index_end.append(next_end)
                i=next_end
            else:
                break
        if len(params_index_beg)==len(params_index_end):
            prev=-1
            for i in range(len(params_index_beg)):
                a=params_index_beg[i]
                b=params_index_end[i]
                if (not prev<a) or (not a<b):
                    error=True
                    break
                else:
                    prev=b
        else:
            error=True
        if error:
            return ('ERROR',None)
        else:
            return ('OK',[f'{text[i+2:j]}' for i,j in zip(params_index_beg,params_index_end)])
