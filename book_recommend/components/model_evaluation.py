from data_validation import tag_processing
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

processed_tags = tag_processing()
ps = PorterStemmer()
stopwords = set(stopwords.words('english'))

corpus = []


for row in processed_tags:
    review = re.sub('[^a-zA-Z0-9]', ' ', row)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords]
    review = ' '.join(review)
    corpus.append(review)

