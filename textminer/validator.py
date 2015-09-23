import re

def binary(i):
    return re.match(r'^(0|1)+$', i)

def binary_even(i):
    return re.match(r'^(0|1)+0$', i)

def hex(i):
    return re.match(r'^[0-9A-F]+$', i)

def word(string):
    return re.match(r'^[0-9a-zA-Z-]*[a-zA-Z]$', string)

def words(string, count=None):
    split_string = re.split(' ', string)
    if count:
        if count != len(split_string):
            return False
        else:
            pass
    if None in [word(string) for string in split_string]:
        return False
    else:
        return True


def phone_number(i):
    return re.match(r'\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}$', i)

def money(i):
     return re.match(r'^\$([0-9]+(,[0-9]{3})*)(\.[0-9]{2})?$', i)

def zipcode(i):
    return re.match(r'^[0-9]{5}(-[0-9]{4})?$', i)

def date(i):
    return re.match(r'^[0-9]{1,4}[/-][0-9]{1,2}[/-][0-9]{2,4}$', i)
