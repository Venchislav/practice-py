def to_freud(sentence):
    res = []
    sentence = sentence.split()
    for i in range(len(sentence)):
        res.append("sex")
    return ' '.join(res)
