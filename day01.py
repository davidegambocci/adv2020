from typing import List
import csv
import time 


#
def solve_01_part1(nr_list: List[int]) -> int:
    """Data una lista, resituisco il prodotto di 2 numeri che sommano a 2020.
    Provo un approccio molto semplice"""
    for index, elem1 in enumerate(nr_list):
        for elem2 in nr_list[index + 1:]:
            if elem1 + elem2 == 2020: 
                return elem1 * elem2

assert solve_01_part1([1721, 979, 366, 299, 675, 1456]) == 514579

#
def solve_01_part2(nr_list: List[int]) -> int:
    """Data una lista, resituisco il prodotto di 3 numeri che sommano a 2020.
    Anche in questo caso, provo un approccio molto semplice"""
    for index1, elem1 in enumerate(nr_list):
        for index2, elem2 in enumerate(nr_list[index1 + 1:]):
            for elem3 in nr_list[index2 + 1:]:
                if elem1 + elem2 + elem3 == 2020: 
                    return elem1 * elem2 * elem3

assert solve_01_part2([1721, 979, 366, 299, 675, 1456]) == 241861950


# carico la lista di input
my_list = []
with open(r"input\day01.csv", newline="\n") as f:
    rdr = csv.reader(f, delimiter=',')
    for line in rdr:
        nr = int(line[0])
        my_list.append(nr)

assert len(my_list) == 200

# # risolvo (1)
# start = time.time()
# print(solve_01_part1(my_list))
# print("TIME (1): ", time.time() - start)

# risolvo (2)
start = time.time()
print(solve_01_part2(my_list))
print("TIME (2): ", time.time() - start)

