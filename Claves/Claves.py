


# In[38]:


import os
import easygui as gui
import pandas as pd
import unicodedata as un


# In[149]:

def clean_string(text:str)->str:
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


# In[150]:


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


# In[148]:


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


# In[129]:

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
                key=[]
            except (IndexError,KeyError):
                result.append(key+char)
                key=[]
    for i in key:
        result.append(i)
    return ''.join(result).strip()


# In[141]:

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

# In[151]:


murcielago('0123456789 murcielagó')


# In[155]:


dametupico('dametupico ademütipóc')
