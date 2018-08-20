from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.preprocessing import Normalizer
from sklearn import metrics
from sklearn.cluster import KMeans, MiniBatchKMeans 
import pandas as pd
import numpy as np
import string
import nltk
#which lemmatize is best how cosine similarity in jython?? as ordered set there is lot to learn nothing
from numpy.linalg import norm
from sklearn.feature_extraction import DictVectorizer
from nltk.corpus import stopwords as stt
import sys
import os
from itertools import *
wordthres=[]
sent=[1,2,3,2,2]  
sen=[0]*5
re=open("answer.txt")
cos=re.read()
ind=cos.find("\n\n")
if ind != -1:
	cos=cos[0:ind]
cos=cos.split("#\n")
print(cos)
status=[]
f=open("res.txt")
anss=ff.read()
ind=anss.find("\n\n")
if ind != -1:
	anss=anss[0:ind]
anss=anss.split("#\n")
print(anss)


for j,aa in enumerate(cos):
	con=aa.split("\n")
	ans=ans[aa]
	ans=ans.split("\n")
	ses=[]
	cosine=[]
	wordor=[]
	for s in sent:
		answ=[]
		ses=[]
		
		if len(temp=[sen.index(x) for x in sen if x == sent.index(s)+1]) == s and len(temp) >1:
			for xx in temp:
				ses=[]
				fin=sen[xx]
				f=open(str(fin)+".txt")
				ff=f.read()
				ind=ff.find("\n\n")
				if ind != -1:
					ff=ff[0:ind]
				ff=ff.split("\n")
				co=con[xx]
				ses=ses.append(co)
				ses=ses+ff
				ses= [  s.lower()  for s in ses]
				ses= [ e.translate(str.maketrans('','',str(string.punctuation)))for e in ses]	
				tfidf_vectorizer = TfidfVectorizer(stop_words='english')
				tfidf_matrix = tfidf_vectorizer.fit_transform(ses)
				ss=cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])
				ss=list(ss)
				s=max(ss)
				answ.append(ss.index(s))
				cu=0
			for k,an in enumerate(answ,old):
				
				if k == 0:
					old.append(an)
				else:
					for o in old if !(old < an):
						cu = -1
						status[j]=-1
						break
					if cu != -1:
						old.append(an)
					else:
						break
						
					
					
					
					
				
	ex=[]			
	for i,co in enumerate(con):			
		an=ans[i]
		print(an)
		file="dreamcode\curious\\"
		f1=open(str(an)+".txt")
		data=f1.read()
		ind=data.find("\n\n")
		dat=data[0:ind]
		dat=dat.split("\n")
		print(dat) #similar word
		ex=ex.append(co)
		ex=ex+dat
		ex= [  e.lower()  for e in ex]
		ex= [ e.translate(str.maketrans('','',str(string.punctuation)))for e in ex]	
		tfidf_vectorizer = TfidfVectorizer(stop_words='english')
		tfidf_matrix = tfidf_vectorizer.fit_transform(ex)
		ss=cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])
		print(ss)
		ss=list(ss)
		cosine=max(ss)
		ansorder=[]
		insorder=[]
		ansc=0
		insc=0
		aa=[0]*100
		cc=0
		store=[]
		count=0	
		wor=[]		
		res=[]
		
		order=[]

	for k2 in ex[1:]:
		k2=nltk.word_tokenize(k2)
		for kk in k2:
			if kk in key:
				order.append(k2.index(kk)+1)
			
			else:
				order.append(0)
			

			
	for k2 in ex[1:]:
		k2=nltk.word_tokenize(k2)
		#insert the code in word co-occurence
		cc += 1
		wor=[]	
		count=0
		ansorder=[]
		insorder=[]
		ansc=1
		insc=1
	 
		for kk in k2:
			insc=1
			if kk not in wor:
				for val in nltk.word_tokenize(ex[0]):
			
					if val== kk:
						#print(val,kk)
						count += 1
						ansorder.append(ansc)
						insorder.append(insc)
						wor.append(kk)
						if count == 2:
							aa[cc-1]=1	
					
						
				
				insc +=1
			ansc += 1
		if aa[cc-1] == 1:
			order=[a_i - b_i for a_i, b_i in zip(insorder, ansorder)]
			sum=[a_i + b_i for a_i, b_i in zip(insorder, ansorder)]
			#print(ansorder,insorder)	
			sum=norm(sum)
			order=norm(order)
			wordord=1-(order/sum)
			wordor=wordor.append(wordord)
		ansorder=[]
		insorder =[]
		count=0
		aa[cc-1] =0
		wor=[]
	ss=list(ss)	
	print(wordor)	
	print(ss.index(max(ss)),wordord.index(max(wordord)))		
