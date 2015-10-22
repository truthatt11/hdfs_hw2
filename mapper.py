#!/usr/bin/env python
import sys
from time import strptime

# input comes from STDIN (stardard input)
for line in sys.stdin:
    # remove leading and tailing whitespace
    line =  line.strip()
    # WHERE TO PARSE TIME
    #split the line into words
    words = line.split(']')
    words = words[0].split('[')
    words = words[1].split()
    words = words[0].split('/')
    time = words[2].split(':')
    month = strptime(words[1], '%b').tm_mon
    if month<10:
        month = '0'+str(month)
#    ptrptime(words[1], '%b').tm_mon
#   r time
    #increase counter
    print '%s-%s-%s %s' % (time[0], month, words[0], time[1])
