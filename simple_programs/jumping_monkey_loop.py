#!/usr/local/bin/python

# Loops give computers a set of instructions that are continually repeated. 
# In a for loop, the computer executes the command for a fixed number of times. 
# In our case, this is defined by the range.
import sys
import time

for x in range(5,0,-1):
    print ('%d little monkeys jumping on the bed, 1 fell off and bumped his head, momma called the doctor and the doctor said, no more monkeys jumping on the bed' % (x) )
    time.sleep(1)

sys.exit()

