def return_words_with_unique_symbols(text):
    # words = text.split()

    # # result_words_with_unique_symbols = []
    # result_words_with_unique_symbols = [word for word in words if len(word) == len(set(word))]


    """
    for word in words:
        if len(word) == len(set(word)):
            result_words_with_unique_symbols.append(word)
    """

    return list(set([word for word in text.split() if len(word) == len(set(word))]))