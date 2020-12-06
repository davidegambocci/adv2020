import csv 


#
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

#
count_valid = 0 
fields_pass = []

#
with open(r'input\day04.txt', newline="\n") as f:
    rdr = csv.reader(f)

    for line in rdr:
        
        #
        if line == []:

            if len(fields) == len(fields_pass):
                count_valid += 1
            
            if 'cid' not in fields_pass and len(fields) == len(fields_pass) + 1:
                count_valid += 1
            
            fields_pass = []
            
        else:
        
            #
            for string in line[0].split(' '):
                for f in fields:
                    if f in string:
                        fields_pass.append(f)


    if len(fields) == len(fields_pass):
        count_valid += 1

    if 'cid' not in fields_pass and len(fields) == len(fields_pass) + 1:
        count_valid += 1



print(count_valid)