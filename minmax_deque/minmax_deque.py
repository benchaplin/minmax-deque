'''
    File name: minmax_deque
    Description: A dynamic deque supporting O(1) min & max operations in O(1) amortized time
    Author: Ben Chaplin
    GitHub: https://github.com/benchaplin/minmax-deque
    Package: minmax_deque
    Python Version: 3.9.10
    License: MIT License Copyright (c) 2022 Ben Chaplin
'''

from collections import deque

''' Methods extend the functionality described:
    https://docs.python.org/3/library/collections.html#collections.deque
'''
class MinMaxDeque:

	def __init__(self):
        self.deque = deque()
        self.mins = deque()
        self.maxes = deque()

    ''' Augmented deque interface
    '''

    def min(self):
        return self.mins[len(mins) - 1]

    def max(self):
        return self.maxes[len(maxes) - 1]

    ''' Original deque interface
    '''

    def append(self, x):
        if x <= self.mins[len(mins) - 1]:
            self.mins.append(x)

        if x >= self.maxes[len(mins) - 1]:
            self.maxes.append(x)

        return self.deque.append(x)

    def appendleft(self, x):
        while (x < self.mins[0]):
            self.mins.popleft()
        self.mins.appendleft(x)

        while (x > self.maxes[0]):
            self.maxes.popleft()
        self.maxes.appendleft(x)

        return self.deque.appendleft(x)
    
    def clear(self):
        self.mins.clear()

        self.maxes.clear()

        return self.deque.clear()

    '''
    def copy(self):
        return self.deque.copy()
        '''

    def count(self, x):
        return self.deque.count(x)

    '''
    def extend(self, it): 
        return self.deque.extend(it)
        '''

    # def index(self...

    '''
    def insert(self, i, x):
        return self.deque.insert(i, x)
        '''

    def pop(self):
        if self.mins[len(mins) - 1] == self.deque[len(self.deque) - 1]:
            self.mins.pop()

        if self.maxes[len(maxes) - 1] == self.deque[len(self.deque) - 1]:
            self.maxes.pop()

        return self.deque.pop()

    def popleft(self):
        self.mins.popleft()
        if self.deque[1] != self.mins[0]:
            self.mins.appendleft(self.deque[1])
            for i in range(2, len(self.deque)):
                if self.deque[i] == self.mins[0]:
                    self.mins.appendleft(self.deque[i])

        self.maxes.popleft()
        if self.deque[1] != self.maxes[0]:
            self.maxes.appendleft(self.deque[1])
            for i in range(2, len(self.deque)):
                if self.deque[i] == self.maxes[0]:
                    self.maxes.appendleft(self.deque[i])

        return self.deque.popleft()

    '''
    def remove(self, value):
        return self.deque.remove(value)
        '''

    # def rotate(self, n=1):

    def maxlen(self):
        return self.deque.maxlen()


