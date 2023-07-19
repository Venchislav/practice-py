from datetime import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    current_date_f = datetime.strptime(current_date, '%B %d, %Y')
    expiration_date_f = datetime.strptime(expiration_date, '%B %d, %Y')
    if type(entered_code) != str or entered_code != correct_code: return False
    return False if current_date_f > expiration_date_f else True
