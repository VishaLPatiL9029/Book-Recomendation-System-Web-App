from book_recommend.components.data_ingestion import books
from book_recommend.components.data_preprocessing import book_process

processed_books = book_process(books)

def tag_processing():
    processed_books['tags'] = processed_books['Title'] + "," + processed_books['Author'] + "," + processed_books['Genre'] + "," + processed_books['SubGenre']
    processed_books['tags'] = processed_books['tags'].apply(lambda x: x.lower())

    return processed_books['tags']




print(processed_books)