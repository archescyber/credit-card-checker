import random
import os
import json
from datetime import datetime

# Clear Terminal.
os.system('cls')
print("""

 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░▒▓████████▓▒░                           
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░                               
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░                               
░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░                               
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░                               
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░                               
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░  ░▒▓█▓▒░                               
                                                                                                   
                                                                                                   
 ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓███████▓▒░                                               
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                                              
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                                              
░▒▓█▓▒░      ░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░                                              
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                                              
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                                              
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░                                               
                                                                                                   
                                                                                                   
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░         
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░         
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓██▓▒░ 
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██▓▒░ 
 """)

# Credit card verification functions
def luhn_check(card_number):
    """ Validate credit card number using Luhn algorithm """
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10 == 0

def is_valid(card_number):
    return luhn_check(card_number)

def is_security_code_valid(card_number, cvv):
    return len(cvv) in [3, 4] and cvv.isdigit()

def is_expiration_date_valid(month, year):
    now = datetime.now()
    exp_date = datetime(year, month, 1)
    return exp_date > now

def get_credit_card_name_by_number(card_number):
    if card_number.startswith('4'):
        return "Visa"
    elif card_number.startswith(('51', '52', '53', '54', '55')):
        return "MasterCard"
    elif card_number.startswith(('9792')):
        return "Troy"

    else:
        return None

# Random data generation function
def randomf(suff):
    code = str(suff['s'])
    possible = suff['z']
    for _ in range(suff['f']):
        code += random.choice(possible)
    return code

# Random credit card information generation function
def generatef():
    data = {
        "thru": {
            "month": '',
            "year": ''
        },
        "cvv2": '',
        "numf": ''
    }

    if data["thru"]["month"] == '' and data["thru"]["year"] == '':
        data["thru"]["month"] = random.choice(['0' + str(x) if x < 10 else str(x) for x in range(1, 13)])
        data["thru"]["year"] = "202" + randomf({"s": '', "z": '123456789', "f": 1})

    if data["cvv2"] == '':
        data["cvv2"] = randomf({"s": '', "z": '1234567890', "f": 3})

    if data["numf"] == '':
        data["numf"] = randomf({"s": '', "z": '1234567890', "f": 16})

    return data

def addf(data):
    with open('data.txt', 'a') as file:
        file.write(json.dumps(data).replace(',', ' ') + '\n')

def checkf(data, allowed_card_types):
    number = data["numf"]
    cvv = data["cvv2"]
    thru = data["thru"]
    conc = f"{thru['month']}/{thru['year'][2:]}"

    card_name = get_credit_card_name_by_number(number)
    if card_name is not None and card_name in allowed_card_types:
        cdata = [{
            "vals": [number, cvv, conc, card_name],
            "data": [is_valid(number), is_security_code_valid(number, cvv), is_expiration_date_valid(int(thru["month"]), int(thru["year"]))]
        }]

        if all(cdata[0]["data"]):
            addf([number, cvv, conc.replace('/', ' '), card_name])

        return cdata
    else:
        return None

def get_user_selection():
    while True:
        print(">   Randomize: 1")
        print(">   Visa: 2")
        print(">   Mastercard: 3")
        print(">   Troy: 4")
        selection = input(">   Select Card Type Number: ").strip()
        if selection == '1':            
            return ['Visa', 'MasterCard', 'Troy']
        elif selection == '2':
            return ['Visa']
        elif selection == '3':
            return ['MasterCard']
        elif selection == '4':
            return ['Troy']
        else:
            print("  Invalid Selection.")


allowed_card_types = get_user_selection()


for _ in range(1000000):
    jsd = checkf(generatef(), allowed_card_types)
    if jsd:
        print(jsd)
