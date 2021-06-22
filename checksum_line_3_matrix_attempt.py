# level 3 - foobar
# soldiers line up single file, in ascending order.
# lines have a fixed size but the numbers taken from each line
# decrease after each check
import time
start_time = time.time()

import numpy as np

def checksum_line(start, length):
    # for start = 0, length = 10,000, the code below takes 37.77 seconds
    #x = list(range(start,length*length+start))

    # for start = 0, length = 10,000, the code below takes .33 seconds!!
    x = np.arange(start, length*length+start)

    # set to zero all of the elements that will be ignored
    x = np.reshape(x, (length,length))
    x = np.flip(x, 1)
    x = np.triu(x, 0)

    # for start = 0, length = 20,000, the code below accounts for 4 seconds,
    # the matrix creation and manipulation above only accouts for 2 seconds worth
    checksum = np.bitwise_xor.reduce(x)
    checksum = np.bitwise_xor.reduce(checksum)
    return checksum



ck = checksum_line(0,20000)
# print(ck)


print("---%s total seconds ---" % (time.time()-start_time))
