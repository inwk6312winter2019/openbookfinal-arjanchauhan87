def sprted_words():
	file = ["a", "the", "at", "run", "to","and","are","or","for","an","this"] 
	wordcount={}
	for word in file():
   	 if word not in wordcount:
            wordcount[word] = 1
   	 else:
      	    wordcount[word] += 1
	for k,v in wordcount.items():
   	 print k, v
