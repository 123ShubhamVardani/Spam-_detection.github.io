from tkinter import *
import string
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
sw=list(ENGLISH_STOP_WORDS)
sw.remove('not')

def removePunc(doc):
	pc=string.punctuation
	clean_doc=re.sub(f'[{pc}]','',doc)
	return clean_doc

df=pd.read_csv('sms.txt',delimiter='\t')
df.columns=['type','msg']
df['msg']=df.msg.apply(removePunc)
cv=CountVectorizer(stop_words=sw)

X=cv.fit_transform(df.msg).todense()
gnb=MultinomialNB()
gnb.fit(X,df.type)	

def mypredict():
	new_rvw=e.get()
	X_test=cv.transform([new_rvw]).todense()
	p=gnb.predict(X_test)
	if(p[0]=='ham'):
                        label=Label(root,text="ham",font=('Book Antiqua' ,25 ,'bold'),bg='white',fg='green')
                        label.place(x=400,y=450)
	else:
                        label=Label(root,text="spam",font=('Book Antiqua' ,25 ,'bold'),bg='white',fg='red')
                        label.place(x=400,y=450)

root=Tk()
root.state('zoomed')
root.resizable(width=False,height=False)
root.configure(background='grey')
l=Label(root,text='Spam Detection',bg='grey',fg='black',font=('cambria',40,'bold'))
l.place(x=550,y=10)

l2=Label(root,text='Enter Msg:',bg='grey',fg='black',font=('cambria',20,'bold'))
l2.place(x=100,y=200)

l3=Label(root,text='',bg='grey',fg='black',font=('cambria',20,'bold'))
l3.place(x=300,y=50)

e=Entry(root,font=('',20,'bold'))
e.place(x=300,y=200)

b=Button(root,command=mypredict,text='Predict',font=('book antiqua',20,'bold'),bg='grey',fg='black')
b.place(x=300,y=300)

root.mainloop()
