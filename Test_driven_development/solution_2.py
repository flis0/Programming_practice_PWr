# Szymon Flis 280153 @flis0 

import re

def Add(numbers: str) -> int | float:
    if type(numbers) != str:
        raise TypeError

    numbers = numbers.replace('\n', ',')

    numbers = numbers.replace(',,', ',0,')

    if numbers == ',':
        return 0

    if re.compile(r'[^0-9,\.-]').match(numbers):
        raise ValueError

    return round(eval(f'sum([{numbers}])'), 10)

if __name__ == '__main__':
    print(type(Add('abc')))