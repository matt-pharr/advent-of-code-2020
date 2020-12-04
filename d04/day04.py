import re

# For this program I heavily referenced a classmate's program to get a feel for the re module!

day = '04'
inp = 'day' + day + 'input.txt'

pspts = 'byr iyr eyr hgt hcl ecl pid'.split()
# Reading function goes here

def validate_existing(puzzle_input:str) -> list:
    validlist = []
    a = puzzle_input.split('\n\n')
    for pspt in a:
        validlist.append('byr' in pspt and 'iyr' in pspt and 'eyr' in pspt and \
                'hgt' in pspt and 'hcl' in pspt and 'ecl' in pspt and \
                    'pid' in pspt)
    return validlist
            
def validate_pspt(puzzle_input:str) -> list:
    a = puzzle_input.split('\n\n')
    validlist = validate_existing(puzzle_input)
    check2list = []
    pspt_list = []

    for i in range(len(a)):
        indict = {}
        for f1 in pspts:
            for field in a[i].split():
                if re.match(f1,field) is not None:
                    indict[field.split(':')[0]] = field.split(':')[1]
        pspt_list.append(indict)

    for i in range(len(a)):
        if validlist[i]:
            passport = pspt_list[i]
            check2list.append(
                re.match(r'^[0-9]{4}',pspt_list[i]['byr']) is not None and 1920 <= int(pspt_list[i]['byr']) <= 2002
                and re.match(r'^[0-9]{4}',pspt_list[i]['iyr']) is not None and 2010 <= int(pspt_list[i]['iyr']) <= 2020
                and re.match(r'^[0-9]{4}',pspt_list[i]['eyr']) is not None and 2020 <= int(pspt_list[i]['eyr']) <= 2030
                and ((re.match(r'^..in',pspt_list[i]['hgt']) is not None and 59 <= int(pspt_list[i]['hgt'][:-2]) <= 76) or
                    (re.match(r'^...cm',pspt_list[i]['hgt']) is not None and 150 <= int(pspt_list[i]['hgt'][:-2]) <= 193)
                ) 
                and pspt_list[i]['ecl'] in 'amb blu brn gry grn hzl oth'.split()
                and re.match(r'^#[0-9a-f]{6}',pspt_list[i]['hcl']) is not None
                and re.match(r'^[0-9]{9}$',pspt_list[i]['pid']) is not None
            )

        else:
            check2list.append(False)
    return check2list

def solve(puzzle_input):
    validlist = validate_existing(puzzle_input)
    validlist1 = validate_pspt(puzzle_input)
    s1 = sum(validlist)
    s2 = sum(validlist1)
    yield s1
    yield s2

if __name__ == "__main__":
    with open(inp) as iofile:
        for s in solve(iofile.read()):
            print(s)