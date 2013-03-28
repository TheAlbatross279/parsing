from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer
import string
import re

def removeStopWords(input_str, rm_words=[]):
    """Removes stopwords defined by NLTK stopwords and removes words from input list, 
    if parameter list is not empty. Method takes as input a list or string, which is split on spaces.""" 
    filtered_msg = []
    #check if string, and split on spaces
    if isinstance(input_str, basestring):
        input_str = tokenize(input_str)
    #check each word against nltk stopwords and specified input list
    for word in input_str:
        if word.lower() not in stopwords.words('english') and word.lower() not in rm_words:
            filtered_msg.append(word)
    return " ".join(filtered_msg)

def normalize(input_str):
    """Takes input and transforms to lower case"""
    filtered_input = []
    #check if string input
    if isinstance(input_str, basestring):
        input_str = input_str.strip()
        input_str = tokenize(input_str)
    for word in input_str:
        word = word.lower()
        filtered_input.append(word)
    return " ".join(filtered_input)

def tokenize(input_str, delims=[]):
    """takes in a string of input and tokenizes it into a list. 
    By default, the string is split on whitespace characters if no delims are specified."""
    delims.append("\s")
    for delim in delims:
        if delim in string.punctuation:
            delim = "\\" + delim
    regex_list = '[%s]' % "|".join(delims)
    tokenizer = RegexpTokenizer(regex_list, gaps=True)
    input_str = tokenizer.tokenize(input_str)
    return input_str

def removePunct(input_str, keep=[]):
    """removes all punctuation from the input except those specified by the keep list parameter."""
    print string.punctuation
    delims = []
    for punct in keep:
        if punct in string.punctuation:
            delims.append("\\%s" % punct)
    keep = delims
    regex = "[^A-Za-z0-9\s ^%s]" % "".join(keep)
    input_str = re.sub(regex, "",input_str)
    print input_str
    return input_str



str = "Hello, my name is the kim-bim. Who are you? Someone special?"
print str
print "NORMALIZE"
print normalize(str)
print "TOKENIZE"
print tokenize(str, delims =["-"])
print"STOP WORDS"
print removeStopWords(str, rm_words=["someone"])
print "REMOVE PUNCT"
print removePunct(str, keep=['?'])
