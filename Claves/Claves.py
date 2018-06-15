import os
import easygui as gui
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
    if 'ñ' in text:
        text2=[]
        for i in text.split('ñ'):
            text2.append(un.normalize('NFKD',i).encode('ascii',errors='ignore').decode('utf-8'))
        return 'ñ'.join(text2)
    else:
        return un.normalize('NFKD',text).encode('ascii',errors='ignore').decode('utf-8')

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
    text=clean_string(texts)
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
    arg_df=pd.DataFrame(data=[list('abcdefghi'),list('jklmnñopq'),list('rstuvwxyz')],index=['i','ii','iii'],columns=['a','n','t','i','l','o','p','e','s'])
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

def morse(text:str)->str:
    result=[]
    abc_str='abcdefghijklmnñopqrstuvwxyz0123456789.,?'
    mor_str=['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
        '.---', '-.-', '.-..', '--', '-.', '--.--', '---', '.--.', '--.-',
        '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
        '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...',
        '---..', '----.', '.-.-.-', '--..--', '..--..']
    text=clean_string(text)
    for char in text:
        if char in '.-/ ':
            morse=True
        else:
            morse=False
            break
    if morse:
        text=text.split('/')
        for i in range(len(text)):
            text[i]=text[i].strip()
        text=' / '.join(text).split(' ')
        for char in text:
            if char in mor_str:
                result.append(abc_str[mor_str.index(char)])
            elif char=='/':
                result.append(' ')
            else:
                result.append(char)
    else:
        for char in text:
            if char in abc_str:
                result.append(mor_str[abc_str.find(char)]+' ')
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
