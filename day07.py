import csv
import networkx as nx
import matplotlib.pyplot as plt
import re

part1 = False
part2 = True

#
#
# -- PART 1 --
#
#

test_dct = {'light red': ['bright white', 'muted yellow'],
            'dark orange': ['bright white', 'muted yellow'],
            'bright white': ['shiny gold'],
            'muted yellow': ['shiny gold', 'faded blue'],
            'shiny gold': ['dark olive', 'vibrant plum'],
            'dark olive': ['faded blue', 'dotted black'],
            'vibrant plum': ['faded blue', 'dotted black'],
            'faded blue': ['no other'],
            'dotted black': ['no other']}


# 
def how_many_connected(d: dict, s: str) -> int:
    G = nx.DiGraph(d)
    # nx.draw(G, with_labels=True)
    # plt.show()
    return [n for n in G.nodes() if nx.has_path(G, n, s) and n != s]


assert len(how_many_connected(test_dct, 'shiny gold')) == 4


#
def modify_str(s: str) -> str:
    smod = s.replace(' bag.', '').replace(' bags.', '').replace(' bags', '').replace(' bag', '')
    return re.sub(r' [0-9] ', '', smod)

#
if part1:
    ind = {}
    with open(f'input/day07.txt') as f:
        rdr = csv.reader(f)
        for line in rdr:
            ls = line[0].split(' bags contain')
            ind.update({ls[0]: [modify_str(ls[1])]})
            for l in line[1:]:
                ind[ls[0]].append(modify_str(l))

    print(len(how_many_connected(ind, 'shiny gold')))

#
#
# -- PART 2 --
#
#

#
def modify_str2(s: str) -> (str, int):
    smod = s.replace(' bag.', '').replace(' bags.', '').replace(' bags', '').replace(' bag', '')
    return re.sub(r' [0-9] ', '', smod), smod[1:2]

#
if part2:
    ind = {}
    with open(f'input/day07.txt') as f:
        rdr = csv.reader(f)
        for line in rdr:
            ls = line[0].split(' bags contain')

            k, v = modify_str2(ls[1])
            if k == ' no other':
                ind.update({ls[0]: []})
            else:
                ind.update({ls[0]: [{k: int(v)}]})
            for l in line[1:]:
                k, v = modify_str2(l)
                ind[ls[0]].append({k: int(v)})


#
test_dct2 = {'light red': [{'bright white': 1}, {'muted yellow': 2}],
            'dark orange': [{'bright white': 3}, {'muted yellow': 4}],
            'bright white': [{'shiny gold': 1}],
            'muted yellow': [{'shiny gold': 2}, {'faded blue': 9}],
            'shiny gold': [{'dark olive': 1}, {'vibrant plum': 2}],
            'dark olive': [{'faded blue': 3}, {'dotted black': 4}],
            'vibrant plum': [{'faded blue': 5}, {'dotted black': 6}],
            'faded blue': [],
            'dotted black': []}

#
def get_bag_nr(d: dict, k: str) -> int:

    if d[k] == []:
        return 0
    
    elif len(d[k]) == 1: 
        print(d[k])

        cond1 = d[k][0]
        k1 = list(cond1.keys())[0]
        v1 = cond1[k1]

        return v1 * (get_bag_nr(d, k1) + 1)
        
    elif len(d[k]) == 2: 
        print(d[k])

        cond1, cond2 = d[k]
        k1, k2 = list(cond1.keys())[0], list(cond2.keys())[0]
        v1, v2 = cond1[k1], cond2[k2]

        return v1 * (get_bag_nr(d, k1) + 1) + v2 * (get_bag_nr(d, k2) + 1)
    
    elif len(d[k]) == 3: 
        print(d[k])

        cond1, cond2, cond3 = d[k]
        k1, k2, k3 = list(cond1.keys())[0], list(cond2.keys())[0], list(cond3.keys())[0]
        v1, v2, v3 = cond1[k1], cond2[k2], cond3[k3]

        return v1 * (get_bag_nr(d, k1) + 1) + v2 * (get_bag_nr(d, k2) + 1) + v3 * (get_bag_nr(d, k3) + 1)
    
    elif len(d[k]) == 4: 
        print(d[k])

        cond1, cond2, cond3, cond4 = d[k]
        k1, k2, k3, k4 = list(cond1.keys())[0], list(cond2.keys())[0], list(cond3.keys())[0], list(cond4.keys())[0]
        v1, v2, v3, v4 = cond1[k1], cond2[k2], cond3[k3], cond4[k4]

        return v1 * (get_bag_nr(d, k1) + 1) + v2 * (get_bag_nr(d, k2) + 1) + v3 * (get_bag_nr(d, k3) + 1) + v4 * (get_bag_nr(d, k4) + 1)


    
# assert get_bag_nr(test_dct2, 'shiny gold') == 32

print(get_bag_nr(ind, 'shiny gold'))