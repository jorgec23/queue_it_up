# level 3 - foobar
# soldiers line up single file, in ascending order.
# lines have a fixed size but the numbers taken from each line
# decrease after each check
import time
start_time = time.time()

def checksum_line(start, length):
    checksum = 0
    for i in range(0,length):
        for j in range(length*i + start, length*(i+1) - i + start):
            checksum ^= j

    return checksum

ck = checksum_line(0,20000)
print(ck)

print("---%s total seconds ---" % (time.time()-start_time))
