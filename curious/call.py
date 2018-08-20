import subprocess

# subprocess.call("java pitt.search.lucene.IndexFilePositions pos")
#subprocess.call("java org.apache.lucene.demo.IndexFiles -docs dreamcode/curious -index ind")
subprocess.call("java pitt.search.semanticvectors.BuildIndex -luceneindexpath ind")
for i in range(100):
	subprocess.call("java pitt.search.semanticvectors.BuildPositionalIndex -luceneindexpath positional_index -windowradius 10 -positionalmethod permutation")
# subprocess.call("java pitt.search.semanticvectors.BuildPositionalIndex -luceneindexpath positional_index -windowradius 10 -positionalmethod  directional")
#Term  pitt.search.semanticvectors.TermVectorsFromLucene 
