import re
import textminer.validator as v

def words(input):
    return v.words(input)

def phone_number(input):
    if v.phone_number(input):
        num = re.sub(r'[^0-9]', '', input)
        return {"area_code" : num[:3], "number" : num[3:6]+'-'+num[6:]}

def money(input):
    if v.money(input):
        mon = re.sub(r'[\,]', '', input)
        return {'currency' : mon[0], 'amount' : float(mon[1:])}

def zipcode(input):
    if v.zipcode(input):
        if len(input) <= 5:
            return {'zip': input[:5], 'plus4': None}
        else:
            return {'zip': input[:5], 'plus4': input[6:]}

def date(input):
    if v.date(input):
        dat = re.split(r'[\/\-]', input)
        dat = [int(x) for x in dat]
        year = sorted(dat)[2]
        return {"month": dat[0], "day": dat[1], "year": year}
