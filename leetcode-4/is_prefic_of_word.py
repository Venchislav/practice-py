def isPrefixOfWord(sentence, searchWord):
    it = (' ' + sentence).find(' ' + searchWord)
    # nice
    return -1 if it == -1 else sentence[:it].count(' ') + 1
