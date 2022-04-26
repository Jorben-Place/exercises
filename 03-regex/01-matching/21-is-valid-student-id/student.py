import re
def is_valid_student_id(string):
    return re.fullmatch('[sSrR]{1}\d{7}', string)