from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from book_recommend.components.data_validation import processed_books
from book_recommend.constant.variables import PICKLE_FILE_PATH
import pickle


#logging.basicConfig(filename='logs/app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

with open(PICKLE_FILE_PATH, 'rb') as file:
    similarity_model = pickle.load(file)

# def recommend(book):
#     book_index = processed_books[processed_books['Title'] == book].index[0]
#     distances = similarity_model[book_index]
#     movie_iist = sorted(list(enumerate(distances)),reverse=True, key= lambda x: x[1])[1:6]
#     for i in movie_iist:
#         print(processed_books.iloc[i[0]].Title)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(processed_books['Title'].values),
                           Author = list(processed_books['Author'].values),
                           Genre = list(processed_books['Genre'].values),
                           SubGenre = list(processed_books['SubGenre'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books',methods = ['POST'])
def recommend():
    user_input = request.form.get('user_input')
    book_index = processed_books[processed_books['Title'] == user_input].index[0]
    distances = similarity_model[book_index]
    movie_iist = sorted(list(enumerate(distances)),reverse=True, key= lambda x: x[1])[1:6]

    data =  []
    # for i in movie_iist:
    #     data.append(processed_books.loc[i].Title)
    # 
    for i in movie_iist:
        item = []
        temp_df = processed_books[processed_books['Title'] == processed_books.iloc[i[0]]['Title']]
        item.extend(list(temp_df.drop_duplicates('Title')['Title'].values))
        item.extend(list(temp_df.drop_duplicates('Title')['Author'].values))
        data.append(item)



    return render_template('recommend.html', data=data)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8080, debug = True)