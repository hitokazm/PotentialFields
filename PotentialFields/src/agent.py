'''
Created on Sep 22, 2012

@author: hitokazu
'''

import random

time_amount = 0


class Agent(object):
    def __init__(self):
        pass
    
    def check_time(self, time_diff):
        limit = random.randint(5) + 3
        time_amount += time_diff
        if time_amount >= limit:
            # Turn left abount 60 degrees
            time_amount = 0
        