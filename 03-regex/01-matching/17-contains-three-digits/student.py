import re
def contains_three_digits(string):
    return re.fullmatch('^(?:\D*\d){3,}\D*$', string)