def predict_age(*args):
    return (sum(i * i for i in args) ** 0.5) // 2
