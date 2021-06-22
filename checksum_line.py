# level 3 - foobar
# soldiers line up single file, in ascending order.
# lines have a fixed size but the numbers taken from each line
# decrease after each check
import time

start_time = time.time()

def checksum_line(start, num_line):
    # take care of lines of size 1
    if num_line == 1:
        return start

    # create a list of the numbers in each line
    all_lines = [list(range(i*num_line + start, (i+1)*num_line +start)) for i in range(0,num_line)]
    print(time.time()-start_time)

    # create a list of the indeces you will keep for each line in the all_lines list
    keep_indeces = [i for i in range(num_line-1, -1, -1)]
    print(time.time()-start_time)

    # create a single list with all of the numbers that will be part of the checksum
    check_indeces = [all_lines[i][0 : keep_indeces[i]+1] for i in range(0, num_line)]
    print(time.time()-start_time)

    # combine the sublists
    check_indeces_flat = [item for sublist in check_indeces for item in sublist]
    print(time.time()-start_time)

    # initialize the checksum
    checksum = check_indeces_flat[0]^check_indeces_flat[1]
    for ind in check_indeces_flat[2:]:
        checksum = checksum^ind

    return checksum
checksum_line(0,10000)


print("---%s total seconds ---" % (time.time()-start_time))
