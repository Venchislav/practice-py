def vowel_indices(word):
    return [c+1 for c, letter in enumerate(word) if letter.lower() in 'aeiouy']
