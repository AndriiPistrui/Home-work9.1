def popular_words(text, words):
    text = text.lower()
    word_list = text.split()

    word_count = {word: 0 for word in words}

    for word in word_list:
        if word in word_count:
            word_count[word] += 1

    return word_count

text = '''When I was One I had just begun When I was Two I was nearly new'''
words = ['i', 'was', 'three', 'near']
print(popular_words(text, words))
