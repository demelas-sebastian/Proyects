import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pythonmail_back as back
from pythonmail_back import Login

class Main(object):
    def __init__(self,window):
        self.window=window
        self.window.wm_title('Automatizador de Mailing - Sebastian Demelas')

        self.v_l_session=tk.StringVar()
        self.v_l_session.set('')
        self.l_session=tk.Label(window,textvariable=self.v_l_session)
        self.l_session.grid(row=0,column=9,sticky='e')

        self.v_b_login_w=tk.StringVar()
        self.v_b_login_w.set('Iniciar sesión...')
        self.b_login_w=tk.Button(window
            ,width=15
            ,command=self.open_login
            ,textvariable=self.v_b_login_w)
        self.b_attach=tk.Button(window
            ,text='Adjuntar archivo...'
            ,width=15)
        self.b_login_w.grid(row=0,column=10)
        self.b_attach.grid(row=1,column=10)

        self.l_body=tk.Label(window,text='Cuerpo del Email:')
        self.l_body.grid(row=2,column=0,sticky='w')

        self.t_body=tk.Text(window,height=6,width=60)
        self.t_body.grid(row=3,column=0,rowspan=6,columnspan=10)

        self.b_close=tk.Button(window
            ,text='Cerrar'
            ,width=10
            ,command=window.destroy)
        self.b_close.grid(row=8,column=10)

    def open_login(self):
        if self.v_b_login_w.get()=='Iniciar sesión...':
            self.top=tk.Toplevel(self.window)
            self.top.title('Log in - Office365')
            Login_window(self.top,self)
        elif self.v_b_login_w.get()=='Cerrar sesión...':
            self.top=tk.Toplevel(self.window)
            self.top.title('Log out')
            Logout_window(self.top,self)

class Login_window(object):
    def __init__(self,window,parent):
        self.window=window
        self.parent=parent

        self.l_user=tk.Label(window,text='Usuario')
        self.l_pass=tk.Label(window,text='Contraseña')
        self.l_user.grid(row=0,column=0,sticky='w')
        self.l_pass.grid(row=2,column=0,sticky='w')

        self.e_user=tk.Entry(window)
        self.e_pass=tk.Entry(window,show='\u2022')
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
        if result=='SUCCESS':
            self.parent.v_b_login_w.set('Cerrar sesión...')
            self.parent.v_l_session.set(self.e_user.get().split('@')[0])
            self.window.destroy()

class Logout_window(object):
    def __init__(self,window,parent):
        self.window=window
        self.parent=parent

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
        self.parent.v_b_login_w.set('Iniciar sesión...')
        self.parent.v_l_session.set('')
        self.window.destroy()

main=tk.Tk()
Main(main)
main.mainloop()
