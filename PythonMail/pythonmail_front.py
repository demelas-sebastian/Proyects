import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pythonmail_back import Login
from pythonmail_back import Mail

class Main(object):
    def __init__(self,window):
        self.window=window
        self.service_name='AutoMailing - Sebastian Demelas'
        self.window.wm_title('AutoMailing - Sebastian Demelas')
        self.mail=Mail(window,self)

        window.protocol('WM_DELETE_WINDOW',self.close)

        self.v_l_session=tk.StringVar()
        self.v_l_session.set('')
        self.l_session=tk.Label(window,textvariable=self.v_l_session)
        self.l_session.grid(row=0,column=9,sticky='e')

        self.v_b_login_w=tk.StringVar()
        self.v_b_attach=tk.StringVar()
        self.v_b_login_w.set('Iniciar sesión...')
        self.v_b_attach.set('Adjuntar archivo...')
        self.b_login_w=tk.Button(window
            ,width=12
            ,command=self.open_login
            ,textvariable=self.v_b_login_w)
        self.b_attach=tk.Button(window
            ,width=15
            ,command=self.attach,
            textvariable=self.v_b_attach)
        self.b_login_w.grid(row=0,column=10)
        self.b_attach.grid(row=5,column=10,sticky='e')

        self.l_to=tk.Label(window,text='Para:',width=1,anchor='w')
        self.l_cc=tk.Label(window,text='CC:',width=1,anchor='w')
        self.l_cco=tk.Label(window,text='CCO:',width=1,anchor='w')
        self.l_att=tk.Label(window,text='Adj.:',width=1,anchor='w')
        self.l_subject=tk.Label(window,text='Asunto:',width=1,anchor='w')
        self.l_to.grid(row=1,column=0,sticky='we')
        self.l_cc.grid(row=2,column=0,sticky='we')
        self.l_cco.grid(row=3,column=0,sticky='we')
        self.l_att.grid(row=4,column=0,sticky='we')
        self.l_att.grid_forget()
        self.l_subject.grid(row=5,column=0,sticky='we')

        self.e_to=tk.Entry(window)
        self.e_cc=tk.Entry(window)
        self.e_cco=tk.Entry(window)
        self.e_att=tk.Entry(window)
        self.e_subject=tk.Entry(window)
        self.e_to.grid(row=1,column=1,sticky='we',columnspan=9)
        self.e_cc.grid(row=2,column=1,sticky='we',columnspan=9)
        self.e_cco.grid(row=3,column=1,sticky='we',columnspan=9)
        self.e_att.grid(row=4,column=1,sticky='we',columnspan=9)
        self.e_att.grid_forget()
        self.e_subject.grid(row=5,column=1,sticky='we',columnspan=9)

        self.l_body=tk.Label(window,text='Cuerpo del Email:',anchor='w')
        self.l_body.grid(row=6,column=0,sticky='we',columnspan=9)

        self.t_body=tk.Text(window,height=6,width=60)
        self.t_body.grid(row=7,column=0,rowspan=6,columnspan=10)

        self.b_send=tk.Button(window
            ,text='Enviar'
            ,width=10
            ,command=self.send_mail)
        self.b_send.grid(row=11,column=10,rowspan=2,sticky='nesw')

    def open_login(self):
        if self.v_b_login_w.get()=='Iniciar sesión...':
            self.top=tk.Toplevel(self.window)
            self.top.title('Log in - Office365')
            Login_window(self.top,self)
        elif self.v_b_login_w.get()=='Cerrar sesión...':
            self.top=tk.Toplevel(self.window)
            self.top.title('Log out')
            Logout_window(self.top,self)

    def send_mail(self):
        if self.e_subject.get()=='':
            msg='No especificó ningun asunto. ¿Desea continuar?'
            title='Ningun asunto'
            if messagebox.askokcancel(parent=self.window,message=msg,title=title):
                self.mail.send_mail()
            else:
                print('cancel')
        else:
            self.mail.send_mail()
            print('sending')

    def clear_fields(self):
        for i in self.window.children.keys():
            if i[:6]=='!entry':
                self.window.children[i].delete(0,tk.END)
            elif i[:5]=='!text':
                self.window.children[i].delete(1.0,tk.END)

    def attach(self):
        if self.v_b_attach.get()=='Adjuntar archivo...':
            self.file_att=filedialog.askopenfilenames(parent=self.window)
            if not self.file_att=='':
                self.mail.attach_file(self.file_att)
                self.l_att.grid(row=4,column=0,sticky='we')
                self.e_att.grid(row=4,column=1,sticky='we',columnspan=9)
                self.b_attach.grid(row=4,column=10,sticky='e')
                self.v_b_attach.set('Retirar archivo')
                self.e_att.delete(0,tk.END)
                self.e_att.insert(tk.END,' | '.join([i.split("/")[-1] for i in self.file_att]))

        elif self.v_b_attach.get()=='Retirar archivo':
            self.l_att.grid_forget()
            self.e_att.grid_forget()
            self.b_attach.grid(row=5,column=10,sticky='e')
            self.v_b_attach.set('Adjuntar archivo...')
            self.e_att.delete(0,tk.END)
            self.e_att.insert(tk.END,'')

    def close(self):
        del self.mail
        self.window.destroy()

class Login_window(Main):
    def __init__(self,window,parent):
        self.window=window
        self.parent=parent
        self.service_name='AutoMailing - Sebastian Demelas'

        self.l_user=tk.Label(window,text='Usuario')
        self.l_pass=tk.Label(window,text='Contraseña')
        self.l_user.grid(row=0,column=0,sticky='w')
        self.l_pass.grid(row=2,column=0,sticky='w')

        self.e_user=tk.Entry(window)
        self.e_pass=tk.Entry(window,show='\u2022',exportselection=0)
        self.e_user.grid(row=1,column=0)
        self.e_pass.grid(row=3,column=0)

        self.b_login=tk.Button(window
            ,text='Iniciar sesión'
            ,width=10
            ,command=self.login)
        self.b_cancel=tk.Button(window
            ,text='Cancelar'
            ,width=10
            ,command=lambda x=window:x.destroy())
        self.b_login.grid(row=1,column=1)
        self.b_cancel.grid(row=3,column=1)

    def login(self):
        result=Login.login(self)
        if result[0]=='SUCCESS':
            self.parent.v_b_login_w.set('Cerrar sesión...')
            self.parent.v_l_session.set(self.e_user.get().split('@')[0])
            self.window.destroy()
        elif result[0]=='AUTH_ERROR':
            messagebox.showerror('Error de autenticación','Error en usuario/contraseña. Por favor vuelva a intentar.')
        elif result[0]=='CRYPT_ERROR':
            messagebox.showerror('Error de encriptación','Error de encriptación. Por favor vuelva a intertar\nSi el problema persiste reinicie su equipo o póngase en contacto con su administrador')
        elif result[0]=='UNKN_ERROR':
            messagebox.showerror('Error desconocido',result[2]+'\n'+result[1])

class Logout_window(Main):
    def __init__(self,window,parent):
        self.window=window
        self.parent=parent
        self.service_name='AutoMailing - Sebastian Demelas'

        self.l_msg=tk.Label(window,text='¿Desea cerrar sesión?')
        self.l_msg.grid(row=0,column=0,columnspan=2)

        self.b_yes=tk.Button(window
            ,text='Si'
            ,width=10,
            command=self.logout)
        self.b_no=tk.Button(window
            ,text='Volver'
            ,width=10
            ,command=window.destroy)
        self.b_yes.grid(row=1,column=0)
        self.b_no.grid(row=1,column=1)

    def logout(self):
        result=Login.logout(self)
        if result[0]=='SUCCESS':
            self.parent.v_b_login_w.set('Iniciar sesión...')
            self.parent.v_l_session.set('')
            self.window.destroy()

main=tk.Tk()
Main(main)
main.mainloop()
