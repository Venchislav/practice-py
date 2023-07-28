def get_number_from_string(string):
    return int(''.join(i for i in list(string) if i.isdigit()))
