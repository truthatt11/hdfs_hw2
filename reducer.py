#!/usr/bin/env python
from operator import itemgetter
import sys
current_word = None
current_time = None
current_count = 0
word = None
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word, time = line.split()

    if current_word == word and current_time == time:
        current_count += 1
    else:
        if current_word:
            print '%s T %s:00:00.000\t%d' % (current_word, current_time, current_count)
        current_count = 1
        current_word = word
        current_time = time

if current_word == word:
    print '%s T %s:00:00.000\t%d' % (current_word, current_time, current_count)
