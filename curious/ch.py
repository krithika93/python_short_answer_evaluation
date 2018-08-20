from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.preprocessing import Normalizer
from sklearn import metrics
from sklearn.cluster import KMeans, MiniBatchKMeans 
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import string
import nltk
#which lemmatize is best how cosine similarity in jython??
from numpy.linalg import norm
from sklearn.feature_extraction import DictVectorizer
from nltk.corpus import stopwords as stt
import sys
import os
"""
folder_list=["pos","cont"] #for initialization
f=open(file1+".txt")
file= [ x for x in range (10)]
file1= str(x[0])
"""
wordthres=[]
sent=[1,2,3,2,2]  #!!!

lmtzr= WordNetLemmatizer()	
print(lmtzr.lemmatize("largest"))
"""
def stem_tokens(tokens, lmtzr):
	stemmed = []
	for item in tokens:
		stemmed.append(lmtzr.lemmatize(item))
		kk=stemmed
	
	return stemmed

def tokenize(text):
	tokens = nltk.word_tokenize(text) 
	return tokens     
"""

from itertools import *
f1=open("1.txt")
data=f1.read()
ind=data.find("\n\n")
dat=data[0:ind]
dat=dat.split("\n")
print(dat) #similar word

ex1=["max equals largest two first two array element used finding biggest array element"]
ex=["largest equals max two first two element array used finding biggest element array"]
"""
elements not present in between check whether 10, 11 present in answer
possorder=[1,2,3,4,[5,6],9,[10,11]]
ind1=[]
l=[]
for i in  possorder:
	if type(i) == "<class 'list'>":
		ind1 = possorder.index(i)
		temp=[]
		temp.append(ind1)
		possorder[i]=list(permutations(i))
		
sa=[]
for l1 in l[0]:
	for l2 in l[1]:
		k=l[0][1]
		k1=l[1][1]
		s=possorder[0:k]+l1+possorder[k+1:k1]+l2+possorder[k1+1:]
		 sa.append(s)
		 to  solve this we need to use recursion, 
		#some words can be or need not be  ,some indices dont matter, i.e if insc = 7,8 it can be continues, or index for those words
		 so comparing a standard example
		 it should match one of the above mentioned word order ,
		 
"""

			
			
			
ex=ex+ex1
ex=ex+dat
print(ex)
ex= [  e.lower()  for e in ex]
ex= [ e.translate(str.maketrans('','',str(string.punctuation)))for e in ex]	
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(ex)
ss=cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])
print(ss)
#lots to take care, finding document and open
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
key=ex[0]
key=nltk.word_tokenize(key)
for k2 in ex[1:]:
	k2=nltk.word_tokenize(k2)
	print(k2)
	if "equals" in k2:
			eq=k2.index("equals")
			prec=k2[eq-1]
			succ=k2[eq+1]
			teq=key.index("equals")
			prec1=key[eq-1]
			succ1=key[eq+1]
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
		print(ansorder,insorder)	
		sum=norm(sum)
		order=norm(order)
		wordord=1-(order/sum)
		res.append(wordord)
	ansorder=[]
	insorder =[]
	count=0
	aa[cc-1] =0
	wor=[]
ss=list(ss)	
print(res)	
print(ss.index(max(ss)),res.index(max(res)))		
