#!/usr/bin/env python

## FRONT MATTER (FUNCTIONS + VARIABLES)
from __future__ import print_function

from datetime import datetime
import socket
import sys
import time

CHECKPOINT_FILENAME = 'fibonacci.checkpoint'
SLEEP_SECONDS = 30
def timestring():
    return datetime.now().strftime('%Y-%m-%h %H:%M:%S')



## STOPPING CONDITION
total_iterations = 10















## INPUT LOGIC + INITIALIZATION
# Figure out where to start from
completed_iterations = 0
n_minus_2 = 0
n_minus_1 = 1
try:
    f = open(CHECKPOINT_FILENAME, 'r')
    completed_iterations = int(f.readline().rstrip())
    n_minus_2 = int(f.readline().rstrip())
    n_minus_1 = int(f.readline().rstrip())
    f.close()
except IOError:
    pass




## DO WORK
# Record information
hostname = socket.gethostname()
print('{}: Starting up on {}, asked to do {} iterations total'.format(timestring(), hostname, total_iterations))
print('{}: Completed iterations = {}'.format(timestring(), completed_iterations))
print('{}: Starting iteration #{}'.format(timestring(), completed_iterations + 1))

# Do Math
new_value = n_minus_2 + n_minus_1
print('{}: Calculated that {} + {} = {}'.format(timestring(), n_minus_2, n_minus_1, new_value))
n_minus_2, n_minus_1 = n_minus_1, new_value
time.sleep(SLEEP_SECONDS)

# Increment iteration counter
completed_iterations += 1


## EXIT LOGIC + CHECKPOINTING/OUTPUT
if (completed_iterations < total_iterations):
    print('{}: Checkpointing'.format(timestring()))
    try:
        f = open(CHECKPOINT_FILENAME, 'w')
        f.write("{}\n{}\n{}\n".format(completed_iterations, n_minus_2, n_minus_1))
        f.close()
    except IOError:
        print('Could not write checkpoint: {}'.format(IOError.strerror))
        sys.exit(2)
    sys.exit(85)

# Write output file and terminate normally
f = open('fibonacci.result', 'w')
f.write("The Fibonacci number after {} iterations is {}\n".format(completed_iterations, new_value))
sys.exit(0)
