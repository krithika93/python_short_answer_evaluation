import sys
import os
from pitt.search.semanticvectors import *
from pitt.search.semanticvectors import BuildIndex
from org.apache.lucene.demo import IndexFiles
from pitt.search.semanticvectors import BuildPositionalIndex
import java.io.IOException
 

"""
file= [ x for x in range (10)]
file1= str(x[0])
f=open(file1+".txt")
folder_list=[]
f=open("1.txt")
data=f.read()
dat=data.splitlines()
thres=[]
sent=[]
for i,d enumerate(dat):
	words=d.split()
	words1=set(words)
"""	
#os.system()
#IndexFiles.main(["-docs", "c:\good\dreamcode\calm\curious"])
#BuildIndex.main(["-luceneindexpath","C:\good\dreamcode\index"])
# BuildIndex.main(["-luceneindexpath","index"])
DEFAULT_VECTOR_FILE = "dreamcode\calm\permtermvectors.bin"
DEFAULT_VECTOR_FILE1= "dreamcode\calm\elementalvectors.bin"
vectorStoreName=""
args=[]
if len(args) == 0:#command line args ?
	
     vectorStoreName = DEFAULT_VECTOR_FILE
     vectorStoreName1 = DEFAULT_VECTOR_FILE1
else:
     vectorStoreName = args[0]
    
defaultFlagConfig = FlagConfig.getFlagConfig(["-searchtype","permutation"])
queryVectorStore  = vectorStoreRam.readFromFile(defaultFlagConfig, vectorStoreName1)
searchVectorStore = VectorStoreRAM.readFromFile(defaultFlagConfig, vectorStoreName)
luceneUtils = None
"""
while true:
	print("Enter a query term:")
	sc = Scanner(System.in).getInstance()
	queryTerm = sc.next()
	

for i,d enumerate(dat):
	words=d.split()
	words1=set(words)
"""
searcher = VectorSearcher.VectorSearcherCosine(queryVectorStore, searchVectorStore, luceneUtils, defaultFlagConfig,["equal", "max"])
results = searcher.getNearestNeighbors(10)
for result in results:
	print(result.getScore(), ":" , result.getObjectVector().getObject())
	realVector = (result.getObjectVector().getVector())
	coordinates = realVector.getCoordinates()
        
		  
		  
	
	
	
	
	









