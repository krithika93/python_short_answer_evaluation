import sys
import os
from pitt.search.semanticvectors import *
import pitt.search.semanticvectors.vectors.RealVector
import pitt.search.semanticvectors.vectors.ZeroVectorException
import java.io.IOException
import java.util.LinkedList
import java.util.Scanner
from pitt.search.semanticvectors import *
from pitt.search.semanticvectors import BuildIndex
from org.apache.lucene.demo import IndexFiles
from pitt.search.semanticvectors import BuildPositionalIndex
import java.io.IOException
#import subprocess
import sys
import os
wordthres=[]
sent=[1,2,3,2,2]
re=open("answer.txt")
con=re.read()
print(con)
"""
ind=con.find("\n\n\n")
con=con[0:ind]
"""
con=con.split()
print(con)
def docfinder(word):
	defaultFlagConfig = FlagConfig.getFlagConfig(None)
	config=None
	vectorStoreName="termvectors.bin"
	vectorStoreName1="docvectors.bin"
	queryVectorStore  = VectorStoreRAM.readFromFile(defaultFlagConfig, vectorStoreName)
	searchVectorStore = VectorStoreRAM.readFromFile(defaultFlagConfig, vectorStoreName1)
	luceneUtils = None
	vecSearcher = VectorSearcher.VectorSearcherCosine( 
                queryVectorStore, searchVectorStore, luceneUtils,defaultFlagConfig,word)
	results = vecSearcher.getNearestNeighbors(10)
	return results[0].getObjectVector().getObject()
"""
for i,words in enumerate(con):
	word = words.split() first index
"""
word=con
print(word)
docs=docfinder(word)
print(docs)
file="dreamcode\curious\\"
file=file+docs
print(file)
f=open("res.txt",'a')
print(str(docs)+" "+str(1)+"\n")
f.write(str(docs)+str(1)+"\n")

key=["largest equals max two first two element array used finding largest element array"]
#init="dreamcode\curious\pos\1"
f=open(file)
#ini = con[0]      #write less code
data=f.read()

ind=data.find("\n\n")
da=data[0:ind]
da=da.split("\n")
#print(ini)
thres=[]
sent=[]
"""
ini = ini.split()
key=nltk.word_tokenize(key)

if "equals" in ini:
	eq=k2.index("equals")
	prec=k2[eq-1]
	succ=k2[eq+1]
	teq=key.index("equals")
	prec1=key[eq-1]
	succ1=key[eq+1]
	if prec1 != prec2  or succ1 != succ:
		wrong=1
	
"""
vectorStoreName=""
args=["?"]
args=args+key[0].split()[1:]
print(args)
#splitlines
vectorStoreName = "permtermvectors.bin"
vectorStoreName1 = "elementalvectors.bin"

defaultFlagConfig = FlagConfig.getFlagConfig(["-searchtype","permutation","-windowradius","10"])
queryVectorStore  = VectorStoreRAM.readFromFile(defaultFlagConfig, vectorStoreName1)
searchVectorStore = VectorStoreRAM.readFromFile(defaultFlagConfig, vectorStoreName)
luceneUtils = None
vec=CompoundVectorBuilder.getPermutedQueryVector(queryVectorStore,luceneUtils,defaultFlagConfig,
                            args)
vec1=args
"""searchvector store in vec
	VectorSearcher
symbols will it work? arr[0]
"""
searcher = VectorSearcher.VectorSearcherCosine(queryVectorStore, searchVectorStore, luceneUtils, defaultFlagConfig,vec)
results = searcher.getNearestNeighbors(10)
for result in results:
	print(result.getScore(), ":" , result.getObjectVector().getObject())
	realVector = result.getObjectVector().getVector()
	realVector = realVector
	coordinates =realVector.getCoordinates()
	coordinates = coordinates
        
		  
		  
	
	
	
	
	










        
	
	
		

