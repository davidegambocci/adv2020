import csv

#
def accept_password_part1(min_char: int, max_char: int, letter: str, password: str) -> int:
    """Verifico la condizione per la password (prima parte)"""
    count = password.count(letter)

    if min_char <= count <= max_char:
        return 1
    else:
        return 0

assert accept_password_part1(1, 3, 'a', 'abcde') == 1
assert accept_password_part1(1, 3, 'b', 'cdefg') == 0
assert accept_password_part1(2, 9, 'c', 'ccccccccc') == 1

#
def accept_password_part2(min_char: int, max_char: int, letter: str, password: str) -> int:
    """Verifico la condizione per la password (seconda parte)"""

    if letter == password[min_char - 1] and letter == password[max_char - 1]:
        return 0
    elif letter != password[min_char - 1] and letter != password[max_char - 1]:
        return 0
    else:
        return 1

assert accept_password_part2(1, 3, 'a', 'abcde') == 1
assert accept_password_part2(1, 3, 'b', 'cdefg') == 0
assert accept_password_part2(2, 9, 'c', 'ccccccccc') == 0



# carico la lista di input
counter1, counter2 = 0, 0
with open(r"input\day02.txt", newline="\n") as f:
    rdr = csv.reader(f, delimiter=',')
    for line in rdr:
        token_split = line[0].split('-')
        space_split = token_split[1].split(' ')
        
        min_char = int(token_split[0])
        max_char = int(space_split[0])
        letter = space_split[1].strip(':')
        password = space_split[2]

        # print(line[0], min_char, max_char, letter, password)
        counter1 += accept_password_part1(min_char=min_char, max_char=max_char, letter=letter, password=password)
        counter2 += accept_password_part2(min_char=min_char, max_char=max_char, letter=letter, password=password)


print('Part 1: ', counter1)
print('Part 2: ', counter2)