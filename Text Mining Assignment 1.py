# coding: utf-8

# read file
text = open('building_global_community.txt').read()

get_ipython().system('pip3 install nltk -U')

import nltk
nltk.download('punkt')

from nltk import wordpunct_tokenize

# normalize words
words = wordpunct_tokenize(text.lower())
# filter out symbols
words1 = [word for word in words if word.isalpha() is True]

# filter out stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

import string
string.punctuation
stopwords.update(string.punctuation)

new_data = [word for word in words1 if word not in stopwords]

# count the occurance of words  
from collections import Counter
counter = Counter(new_data)
counter.most_common(20)
