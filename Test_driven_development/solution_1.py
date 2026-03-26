# Iwo Chwiszczuk 280043 @iwonieevo

def Add(numbers: str):
    numbers_splitted = numbers.replace('\n', ',').split(',')
    ret = 0
    for num in numbers.replace('\n', ',').split(','):
        if num.replace('.','').replace('-', '').isnumeric():
            ret += float(num) if '.' in num else int(num)
        elif len(num.rstrip()) == 0:
            continue
        else:
            raise(ValueError)
    return round(ret, 9)

if __name__ == '__main__':
    pass