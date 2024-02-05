def book_process(text):
    #text.reset_index(inplace=True)
    text.drop('Publisher', axis=1, inplace=True)
    text.drop('Height', axis=1, inplace=True)
    text.dropna(inplace=True)
    return text


