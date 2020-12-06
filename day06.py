import csv
import string

#
def count_ans_group(group: str) -> int:
    """Conta quante risposte"""
    return len(set(w for w in group))

assert count_ans_group('abc') == 3 
assert count_ans_group('abac') == 3 

#
def count_ans_group(group: str) -> int:
    """Conta quante risposte"""
    return len(set(w for w in group))

assert count_ans_group('abc') == 3 
assert count_ans_group('abac') == 3 


# # Prima parte
# allstr = ''
# with open(r'input\day06.txt') as f:
#     rdr = csv.reader(f)
#     for line in rdr:
#         try:
#             allstr += line[0]
#         except IndexError:
#             allstr += ' '
#


allstr, singlestr = '', string.ascii_lowercase
with open(r'input\day06.txt') as f:
    rdr = csv.reader(f)
    for line in rdr:
        try:
            singlestr = ''.join(set(singlestr).intersection(line[0]))
        except IndexError:
            allstr += singlestr + ' '
            singlestr = string.ascii_lowercase
    
    allstr += singlestr + ' '



print(sum(count_ans_group(x) for x in allstr.split(' ')))





