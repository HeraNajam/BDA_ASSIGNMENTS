"""
Q1) Write a program that will have a dictionary object with the following data, given below. The
names which starts with ‘a’ to ‘g’ should concatenate Mr. In starting of the name and for the rest
of the letters, concatenate Ms. In starting of the name. Then remove the person data if his/her
name starts with ’s’,’m’ or ‘k’, Also, calculate the year in which a person is bornt, derived from
age.After that sum the total amount of deposits in an array. Finally, just write the data to json file.
"""
import json
def get_alphabets():
    alphabets = [chr(i) for i in range(97, 123) if chr(i) not in ['s','m','k']]
    # print(alphabets)
    return tuple(alphabets)
    
def get_alphabets_2():
    alphabets = [chr(i) for i in range(97, 123) if chr(i) not in ['a','b', 'c','d','e','f','g']]
    return tuple(alphabets)

titleHelper1 = lambda personDict: personDict.update({'name': 'Ms. ' +personDict['name']
if personDict['name'].lower().startswith(get_alphabets_2())
else 'Mr. ' +personDict['name']}) or personDict

def addMrOrMs(elements):
    elementsWithMrOrMs = {k: titleHelper1(v) for k, v in elements.items()}
    return elementsWithMrOrMs
    
def filter_condition(elementWithMrOrMs):
      lmFun = lambda x: str(x[1]['name'].split(' ')[1])[0].lower().startswith(get_alphabets())
      result = lmFun(elementWithMrOrMs)
      return result

titleHelper2 = lambda personDict: personDict.update({'year': 2020 - personDict['age']}) or personDict

def cal_year(elements):
    calyear = {k: titleHelper2(v) for k, v in elements.items()}
    return calyear

titleHelper3 = lambda personDict: personDict.update({'amount_deposited': personDict['amount_deposited'][0]
                                                                         + personDict['amount_deposited'][1]}) or personDict
def cal_total_amount(elements):
    caltotalamount = {k: titleHelper3(v) for k,v in elements.items()}
    return caltotalamount

def processing(elements):
    elementsWithMrOrMs = addMrOrMs(elements)
    res = filter(filter_condition, elementsWithMrOrMs.items())
    res_1 = cal_year(dict(res))
    res_2 = cal_total_amount(res_1)
    return res_2

def main():
    My_Dict = {
    'person_1': {'name': 'Abdul Rafay',
                 'age': 22,
                 'Interests': ['football', 'cricket'],
                 'amount_deposited': [24000, 26000]},
    'person_2': {'name': 'Nancy James',
                 'age': 23,
                 'Interests': ['baseball', 'cricket'],
                 'amount_deposited': [24000,27000]},
    'person_3': {'name': 'Selena Gomez',
                 'age': 26,
                 'Interests': ['baseball', 'table tennis'],
                 'amount_deposited': [24000,28000]}
    }
    result = processing(My_Dict)
    dic_1 = {
        'current_Date': '21-Nov-2020',
        'Data': result
    }
    print(dic_1)
    with open('names.json', 'w') as file:
        json.dump(dic_1, file, indent=2, sort_keys=False)
        print('The file has been saved')

if __name__ == '__main__':
    main()