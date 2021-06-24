# level 3 - foobar
# soldiers line up single file, in ascending order.
# lines have a fixed size but the numbers taken from each line
# decrease after each check
import time
import numpy as np
start_time = time.time()


def checksum_line(start, length):
    # first person in each line that is checked
    starting_points = [start + length*i for i in range(0, length)]
    # last person in each line that is checked
    ending_points = [start + length*(i+1)-i-1 for i in range(0, length)]
    # xor of each line of workers that is checked, note that with xor algebra, you only need these two numbers, not the entire list
    xor_row = [xor_all_natural(ending_points[i])^xor_all_natural(starting_points[i]-1)  for i in range(0,length)]

    # xor of the xor for each line
    checksum = np.bitwise_xor.reduce(xor_row)

    return checksum


def xor_all_natural(n):
    # this function calculates the xor of any list from 1 to n
    if n%4 == 0:
        return n
    elif n%4 == 1:
        return 1
    elif n%4 == 2:
        return n+1
    else:
        return 0


ck = checksum_line(0,100000)
print(ck)


print("---%s total seconds ---" % (time.time()-start_time))
