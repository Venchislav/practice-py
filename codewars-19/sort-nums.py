def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: list(filter(str.isdigit, x))[0]))
  
