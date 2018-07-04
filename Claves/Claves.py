import tkinter as tk
import pandas as pd
import unicodedata as un

def clean_string(text:str)->str:
    t=[]
    for char in text:
        if ord(char)==8211:
            t.append(chr(45))
        else:
            t.append(char)
    text=''.join(t)
    text=text.lower().strip()
    text2=[]
    for i in text.split('ñ'):
        text2.append(un.normalize('NFKD',i).encode('ascii',errors='ignore').decode('utf-8'))
    return 'ñ'.join(text2)

def murcielago(text:str)->str:
    murcielago_str='murcielago'
    text=clean_string(text)
    result=[]
    for char in text:
        if char in murcielago_str:
            result.append(str(murcielago_str.find(char)))
        elif ord(char) in range(48,58):
            result.append(murcielago_str[ord(char)-48])
        else:
            result.append(char)
    return ''.join(result)

def carlina_betfuse(text:str)->str:
    result=[]
    carlina_str='carlina'
    betfuse_str='betfuse'
    text=clean_string(text)
    for char in text:
        if char in carlina_str:
            result.append(betfuse_str[carlina_str.find(char)])
        elif char in betfuse_str:
            result.append(carlina_str[betfuse_str.find(char)])
        else:
            result.append(char)
    return ''.join(result)

def baden_powel(text:str)->str:
    result=[]
    baden_str='baden'
    powel_str='powel'
    text=clean_string(text)
    for char in text:
        if char in baden_str:
            result.append(powel_str[baden_str.find(char)])
        elif char in powel_str:
            result.append(baden_str[powel_str.find(char)])
        else:
            result.append(char)
    return ''.join(result)

def dametupico(text:str)->str:
    result=[]
    dm_str='dmtpc'
    ae_str='aeuio'
    text=clean_string(text)
    for char in text:
        if char in dm_str:
            result.append(ae_str[dm_str.find(char)])
        elif char in ae_str:
            result.append(dm_str[ae_str.find(char)])
        else:
            result.append(char)
    return ''.join(result)

def palerinofu (text:str)->str:
    result=[]
    pl_str='plrnf'
    ae_str='aeiou'
    text=clean_string(text)
    for char in text:
        if char in pl_str:
            result.append(ae_str[pl_str.find(char)])
        elif char in ae_str:
            result.append(pl_str[ae_str.find(char)])
        else:
            result.append(char)
    return ''.join(result)

def inversa(text:str)->str:
    result=[]
    inversa_str='abcdefghijklmn'
    asrevni_str='zyxwvutsrqpoñn'
    text=clean_string(text)
    for char in text:
        if char in inversa_str:
            result.append(asrevni_str[inversa_str.find(char)])
        elif char in asrevni_str:
            result.append(inversa_str[asrevni_str.find(char)])
        else:
            result.append(char)
    return ''.join(result)

''' Deprecated
def argentina2_decode(text:str)->str:
    result=[]
    key=[]
    arg_df=pd.DataFrame(data=[list('abcdefghi'),list('jklmnñopq'),list('rstuvwxyz')],index=['i','ii','iii'],columns=['a','r','g','e','n','t','i+','n2','a2'])
    text=clean_string(text)
    for char in text:
        if char in 'argentina2':
            key.append(char)
        elif char=='/':
            key=''.join(key)
            if (key=='ii') or (key=='iii') or (key=='iiii'):
                result.append(arg_df.loc[key[1:],'i+'])
            else:
                result.append(arg_df.loc[key[key.find('i'):],key[:key.find('i')]])
            key=[]
        else:
            result.append(char)
    return ''.join(result)
'''
''' Deprecated
def argentina3_decode(text:str)->str:
    result=[]
    key=[]
    arg_df=pd.DataFrame(data=[list('abcdefghi'),list('jklmnñopq'),list('rstuvwxyz')],index=['i','ii','iii'],columns=['a','r','g','e','n','t','i','n2','a2'])
    text=clean_string(text)
    for char in text:
        if char in 'argentina2':
            key.append(char)
        elif char=='/':
            key=''.join(key)
            try:
                if not key[1].isdigit():
                    result.append(arg_df.loc[key[1:],key[0]])
                else:
                    result.append(arg_df.loc[key[2:],key[:2]])
            except IndexError:
                result.append(char)
            except KeyError as ke:
                print(''.join(result)+' --- '+key)
                raise ke
            key=[]
        else:
            result.append(char)
    return ''.join(result)
'''

def argentina_decode(text:str)->str:
    result=[]
    key=[]
    arg_df=pd.DataFrame(data=[list('abcdefghi'),list('jklmnñopq'),list('rstuvwxyz')],index=['i','ii','iii'],columns=['a','r','g','e','n','t','i','n2','a2'])
    text=clean_string(text)
    for char in text:
        if char==' ':
            for i in ''.join(key)+char:
                result.append(i)
            key=[]
        elif char!='/':
            key.append(char)
        else:
            key=''.join(key)
            try:
                if not key[1].isdigit():
                    result.append(arg_df.loc[key[1:],key[0]])
                else:
                    result.append(arg_df.loc[key[2:],key[:2]])
            except (IndexError,KeyError):
                result.append(key+char)
            finally:
                key=[]
    for i in key:
        result.append(i)
    return ''.join(result).strip()

''' Deprecated
def argentina2_encode(text:str)->str:
    result=[]
    arg_df=pd.DataFrame(data=[list('abcdefghi'),list('jklmnñopq'),list('rstuvwxyz')],index=['i','ii','iii'],columns=['a','r','g','e','n','t','i+','n2','a2'])
    text=clean_string(text)
    for char in text:
        found=False
        for i in range(len(arg_df.index)):
            for j in range(len(arg_df.columns)):
                if arg_df.iloc[i,j]==char:
                    found=True
                    if arg_df.columns[j]=='i+':
                        result.append('i{}/'.format(arg_df.index[i]))
                    else:
                        result.append('{}{}/'.format(arg_df.columns[j],arg_df.index[i]))
        if found==False:
            result.append(char)
    return ''.join(result)
'''

def argentina_encode(text:str)->str:
    result=[]
    arg_df=pd.DataFrame(data=[list('abcdefghi'),list('jklmnñopq'),list('rstuvwxyz')],index=['i','ii','iii'],columns=['a','r','g','e','n','t','i','n2','a2'])
    text=clean_string(text)
    for char in text:
        found=False
        for i in range(len(arg_df.index)):
            for j in range(len(arg_df.columns)):
                if arg_df.iloc[i,j]==char:
                    found=True
                    result.append(f'{arg_df.columns[j]}{arg_df.index[i]}/')
        if found==False:
            result.append(char)
    return ''.join(result)

def antilopes_decode(text:str)->str:
    result=[]
    key=[]
    ant_df=pd.DataFrame(data=[list('abcdefghi'),list('jklmnñopq'),list('rstuvwxyz')],index=['i','ii','iii'],columns=['a','n','t','i','l','o','p','e','s'])
    text=clean_string(text)
    for char in text:
        if char==' ':
            for i in ''.join(key)+char:
                result.append(i)
            key=[]
        elif char!='/':
            key.append(char)
        else:
            key=''.join(key)
            try:
                result.append(ant_df.loc[key[1:],key[0]])
            except (IndexError,KeyError):
                result.append(key+char)
            finally:
                key=[]
    for i in key:
        result.append(i)
    return ''.join(result).strip()

def antilopes_encode(text:str)->str:
    result=[]
    ant_df=pd.DataFrame(data=[list('abcdefghi'),list('jklmnñopq'),list('rstuvwxyz')],index=['i','ii','iii'],columns=['a','n','t','i','l','o','p','e','s'])
    text=clean_string(text)
    for char in text:
        found=False
        for i in range(len(ant_df.index)):
            for j in range(len(ant_df.columns)):
                if ant_df.iloc[i,j]==char:
                    found=True
                    result.append(f'{ant_df.columns[j]}{ant_df.index[i]}/')
        if found==False:
            result.append(char)
    return ''.join(result)

def morse_decode(text:str)->str:
    result=[]
    abc_str='abcdefghijklmnñopqrstuvwxyz0123456789.,?'
    mor_l=['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
        '.---', '-.-', '.-..', '--', '-.', '--.--', '---', '.--.', '--.-',
        '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
        '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...',
        '---..', '----.', '.-.-.-', '--..--', '..--..']
    text=clean_string(text).split('/')
    for i in range(len(text)):
        text[i]=text[i].strip()
    text=' / '.join(text).split(' ')
    for char in text:
        if char in mor_l:
            result.append(abc_str[mor_l.index(char)])
        elif char=='/':
            result.append(' ')
        else:
            result.append(char)
    return ''.join(result)

def morse_encode(text:str)->str:
    result=[]
    abc_str='abcdefghijklmnñopqrstuvwxyz0123456789.,?'
    mor_l=['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
        '.---', '-.-', '.-..', '--', '-.', '--.--', '---', '.--.', '--.-',
        '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
        '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...',
        '---..', '----.', '.-.-.-', '--..--', '..--..']
    text=clean_string(text)
    for char in text:
        if char in abc_str:
            result.append(mor_l[abc_str.find(char)]+' ')
        elif char==' ':
            result.append(' / ')
        else:
            result.append(char)
    return ''.join(result)

def brujula_encode(text:str)->str:
    result=[]
    brj_df=pd.DataFrame(data=[list('aeimptx'),list('bfjnquy'),list('cgkñrvz'),list('dhlosw')],index=['N','E','S','O'],columns=[f'{i}' for i in range(1,8)])
    text=clean_string(text)
    for char in text:
        found=False
        for i in range(len(brj_df.index)):
            for j in range(len(brj_df.columns)):
                if brj_df.iloc[i,j]==char:
                    found=True
                    result.append(f'{brj_df.columns[j]}{brj_df.index[i]}/')
        if found==False:
            result.append(char)
    return ''.join(result)

def brujula_decode(text:str)->str:
    result=[]
    key=[]
    brj_df=pd.DataFrame(data=[list('aeimptx'),list('bfjnquy'),list('cgkñrvz'),list('dhlosw')],index=['N','E','S','O'],columns=[f'{i}' for i in range(1,8)])
    text=clean_string(text)
    text=text.upper()
    for char in text:
        if char==' ':
            for i in ''.join(key)+char:
                result.append(i)
            key=[]
        elif char!='/':
            key.append(char)
        else:
            key=''.join(key)
            try:
                result.append(brj_df.loc[key[1],key[0]])
            except (IndexError,KeyError):
                result.append(key+char)
            finally:
                key=[]
    for i in key:
        result.append(i)
    return ''.join(result).strip()

def execute_command():
    t_salida.delete(1.0,tk.END)
    if v_clave.get()==1:
        t_salida.insert(tk.END,murcielago(t_entrada.get(1.0,tk.END)))
    elif v_clave.get()==2:
        t_salida.insert(tk.END,carlina_betfuse(t_entrada.get(1.0,tk.END)))
    elif v_clave.get()==3:
        t_salida.insert(tk.END,baden_powel(t_entrada.get(1.0,tk.END)))
    elif v_clave.get()==4:
        t_salida.insert(tk.END,dametupico(t_entrada.get(1.0,tk.END)))
    elif v_clave.get()==5:
        t_salida.insert(tk.END,palerinofu(t_entrada.get(1.0,tk.END)))
    elif v_clave.get()==6:
        t_salida.insert(tk.END,inversa(t_entrada.get(1.0,tk.END)))
    elif v_clave.get()==7:
        if v_accion.get()==1:
            t_salida.insert(tk.END,argentina_encode(t_entrada.get(1.0,tk.END)))
        elif v_accion.get()==2:
            t_salida.insert(tk.END,argentina_decode(t_entrada.get(1.0,tk.END)))
        else:
            t_salida.insert(tk.END,'Error identificando acción')
    elif v_clave.get()==8:
        if v_accion.get()==1:
            t_salida.insert(tk.END,antilopes_encode(t_entrada.get(1.0,tk.END)))
        elif v_accion.get()==2:
            t_salida.insert(tk.END,antilopes_decode(t_entrada.get(1.0,tk.END)))
        else:
            t_salida.insert(tk.END,'Error identificando acción')
    elif v_clave.get()==9:
        if v_accion.get()==1:
            t_salida.insert(tk.END,morse_encode(t_entrada.get(1.0,tk.END)))
        elif v_accion.get()==2:
            t_salida.insert(tk.END,morse_decode(t_entrada.get(1.0,tk.END)))
        else:
            t_salida.insert(tk.END,'Error identificando acción')
    elif v_clave.get()==10:
        if v_accion.get()==1:
            t_salida.insert(tk.END,brujula_encode(t_entrada.get(1.0,tk.END)))
        elif v_accion.get()==2:
            t_salida.insert(tk.END,brujula_decode(t_entrada.get(1.0,tk.END)))
        else:
            t_salida.insert(tk.END,'Error identificando accion')
    else:
        t_salida.insert(tk.END,'Error identificando clave')

def close(master):
    master.destroy()
    exit()

window=tk.Tk()
window.wm_title('Claves Scout por Sebastian Demelas')

l_claves=tk.Label(window,text='Claves:')
l_accion=tk.Label(window,text='Acción:')
l_entrada=tk.Label(window,text='Entrada:')
l_salida=tk.Label(window,text='Salida:')
l_claves.grid(row=0,column=0)
l_accion.grid(row=3,column=0)
l_entrada.grid(row=5,column=0)
l_salida.grid(row=7,column=0)

v_clave=tk.IntVar()
r_murcielago=tk.Radiobutton(window,text='Murciélago',variable=v_clave,value=1)
r_carlina=tk.Radiobutton(window,text='Carlina Betfuse',variable=v_clave,value=2)
r_baden=tk.Radiobutton(window,text='Baden Powel',variable=v_clave,value=3)
r_dametupico=tk.Radiobutton(window,text='Dametupico',variable=v_clave,value=4)
r_palerinofu=tk.Radiobutton(window,text='Palerinofu',variable=v_clave,value=5)
r_inversa=tk.Radiobutton(window,text='Inversa',variable=v_clave,value=6)
r_argentina=tk.Radiobutton(window,text='Argentina',variable=v_clave,value=7)
r_antilopes=tk.Radiobutton(window,text='Antilopes',variable=v_clave,value=8)
r_morse=tk.Radiobutton(window,text='Morse',variable=v_clave,value=9)
r_brujula=tk.Radiobutton(window,text='Brújula',variable=v_clave,value=10)
r_murcielago.grid(row=1,column=0)
r_carlina.grid(row=1,column=1)
r_baden.grid(row=1,column=2)
r_dametupico.grid(row=1,column=3)
r_palerinofu.grid(row=1,column=4)
r_inversa.grid(row=2,column=0)
r_argentina.grid(row=2,column=1)
r_antilopes.grid(row=2,column=2)
r_morse.grid(row=2,column=3)
r_brujula.grid(row=2,column=4)

v_accion=tk.IntVar()
r_encode=tk.Radiobutton(window,text='Codificar',variable=v_accion,value=1)
r_decode=tk.Radiobutton(window,text='Decodificar',variable=v_accion,value=2)
r_encode.grid(row=4,column=0)
r_decode.grid(row=4,column=1)

t_entrada=tk.Text(window,height=6,width=60)
t_salida=tk.Text(window,height=6,width=60)
t_entrada.grid(row=6,column=0,columnspan=10)
t_salida.grid(row=8,column=0,columnspan=10)

scrl_entrada=tk.Scrollbar(window)
scrl_salida=tk.Scrollbar(window)
scrl_entrada.grid(row=6,column=10)
scrl_salida.grid(row=8,column=10)

t_entrada.configure(yscrollcommand=scrl_entrada.set)
t_salida.configure(yscrollcommand=scrl_salida.set)
scrl_entrada.configure(command=t_entrada.yview)
scrl_salida.configure(command=t_salida.yview)

b_ejecutar=tk.Button(window,text='Ejecutar',command=execute_command,width=12)
b_close=tk.Button(window,text='Cerrar',command=lambda x=window:close(x))
b_ejecutar.grid(row=6,column=11)
b_close.grid(row=8,column=11)

window.mainloop()
