import pandas as pd
import re
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features= 50, stop_words='english')
from sklearn.metrics.pairwise import cosine_similarity