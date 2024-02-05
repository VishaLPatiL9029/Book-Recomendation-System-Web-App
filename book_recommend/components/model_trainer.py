import pandas as pd
import pickle
from data_ingestion import books
from model_evaluation import corpus
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df = pd.DataFrame({'Text': corpus})



cv = CountVectorizer(max_features= 50, stop_words='english')
vector = cv.fit_transform(df['Text']).toarray()
similarity = cosine_similarity(vector)


with open('cosine_similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)

