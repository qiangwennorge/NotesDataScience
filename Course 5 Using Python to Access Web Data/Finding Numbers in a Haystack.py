import re


#fname = 'regex_sum_42.txt'

fname = 'regex_sum_49601.txt'

sum_num = 0

fh = open(fname)
for line in fh:
    numbers_in_line = re.findall(r'[0-9]+', line)
    sum_num += sum([int(num) for num in numbers_in_line])


print(sum_num)
 
