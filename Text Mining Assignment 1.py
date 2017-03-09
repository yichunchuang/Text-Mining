
# coding: utf-8

# In[63]:

text = open('building_global_community.txt').read()


# In[64]:

get_ipython().system('pip3 install nltk -U')


# In[65]:

import nltk
nltk.download('punkt')


# In[159]:

from nltk import wordpunct_tokenize


# In[168]:

words = wordpunct_tokenize(text.lower())


# In[206]:

words1 = [word for word in words if word.isalpha() is True]


# In[207]:

nltk.download('stopwords')


# In[208]:

from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))


# In[209]:

import string
string.punctuation
stopwords.update(string.punctuation)


# In[213]:

# for word in words:
#     if word not in stopwords:
#         print(word)
new_data = [word for word in words1 if word not in stopwords]


# In[214]:

from collections import Counter
counter = Counter(new_data)


# In[215]:

counter.most_common(20)


# In[216]:




# In[ ]:



