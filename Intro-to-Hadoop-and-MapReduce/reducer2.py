# Your task is to make sure that this mapper code does not fail on corrupt data lines,
# but instead just ignores them and continues working

from itertools import groupby
from operator import itemgetter
import sys


def reducer():

    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")

        if len(data) != 2:
            #something has gone wrong
            continue

        #this_store, this_sale = data

        for current_store, group in groupby(data, itemgetter(0)):
            try:
                max_sale = max(float(itemgetter(1)) for current_store, this_store in group)
                print "{0}\t{1}".format(current_store, max_sale)
            except valueError:
                #itemgetter not a float so discard silently
                pass
