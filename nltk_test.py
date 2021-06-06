import nltk
from nltk import word_tokenize
text = word_tokenize("I like to ride bicycles")
output = nltk.pos_tag(text)
print(output)
