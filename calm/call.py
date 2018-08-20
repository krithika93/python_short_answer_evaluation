import subprocess
subprocess.call("java pitt.search.lucene.IndexFilePositions curious")
subprocess.call("java pitt.search.semanticvectors.BuildPositionalIndex -luceneindexpath positional_index -windowradius 5 -positionalmethod permutation")
