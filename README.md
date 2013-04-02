parsing
=======

Python parsing code to clean input for processing.

###Functions
#####normalize(input_str)
   Takes input and transforms to lower case.

#####removePunct(input_str, keep=[])
  Removes all punctuation from the input except those specified by the keep list parameter.

#####removeStopWords(input_str, rm_words=[])
  Removes stopwords defined by NLTK stopwords and removes words from input list, 
  if parameter list is not empty. 
 
  Method takes as input a list or string, which is split on spaces.

#####tokenize(input_str, delims=[r'\s', r'\s'])

  Takes in a string of input and tokenizes it into a list. 
 
  By default, the string is split on whitespace characters if no delims are specified.
