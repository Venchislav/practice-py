def hello(*args):
    return f'Hello, {args[0].capitalize()}!' if len(args) > 0 and args[0] != "" else 'Hello, World!'


# but better

def hello(name=""):
    return f"Hello, {name.capitalize() if name else 'World'}!"
