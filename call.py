import subprocess
subprocess.call("java pitt.search.lucene.IndexFilePositions pos")
subprocess.call("java pitt.search.semanticvectors.BuildPositionalIndex -luceneindexpath positional_index -windowradius 20 -positionalmethod permutation")
# subprocess.call("java pitt.search.semanticvectors.BuildPositionalIndex -luceneindexpath positional_index -windowradius 10 -positionalmethod  directional")
#Term  pitt.search.semanticvectors.TermVectorsFromLucene 
