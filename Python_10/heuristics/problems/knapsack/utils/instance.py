# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:00:21 2021

Use this class to represent knapsack instances.

@author: beer
"""

import heuristics.problems.knapsack.utils.item as it


class Instance:
    NUM_ITEMS_INDEX = 0
    CAPACITY_INDEX = 1

    num_items = 0
    capacity = 0.
    weight = 0.
    value = 0.
    items = []
    itemflags = []

    def __init__(self, *args):
  
        # if there are 6 args: create instance from data in args
        if len(args) == 6:
            if isinstance(args[0], int) and isinstance(args[1], float) and isinstance(args[2], float) and isinstance(args[3], float) and isinstance(args[4], list) and isinstance(args[5], list):
                self.num_items = args[0]
                self.capacity = args[1]
                self.weight = args[2]
                self.value = args[3]
                self.items = args[4][:]
                self.itemflags = args[5][:]
            else:
                print("hi!")
                raise ValueError

        # if there is 1 arg: create instance from given file
        # structure of file: 
        #      number of items
        #      capacity of knapsack
        #      weights of items, one per line
        #      values of items, one per line
        elif isinstance(args[0], str):
            try:
                with open(args[0]) as f:
                    lines = f.readlines()
            except OSError as err:
                print('OS error: {0}'.format(err))

            header = lines[0:2]
            self.num_items = int(header[self.NUM_ITEMS_INDEX].split()[0])
            self.capacity = float(header[self.CAPACITY_INDEX].split()[0])
                    
            self.items = []
            lines = [line for line in lines[2:] if line.strip()]
            if len(lines) != 2*self.num_items:
                raise ValueError
            else:
                for k in range(self.num_items):
                    item = it.Item(float(lines[k].split()[0]), float(lines[self.num_items + k].split()[0]))
                    self.items.append(item)
                    self.itemflags.append(False)
        
        else:
            raise ValueError


    def getNumItems(self):
        return self.num_items


    def getCapacity(self):
        return self.capacity


    def getWeight(self):
        return self.weight


    def setWeight(self, weight):
        self.weight = weight
        return

        
    def addToWeight(self, weight):
        self.weight += weight
        return


    def getValue(self):
        return self.value


    def setValue(self, value):
        self.value = value
        return


    def addToValue(self, value):
        self.value += value
        return
    
 
    def getItemFlag(self, itemNum):
        return self.itemflags[itemNum]
        

    def setItemFlag(self, itemNum):
        self.itemflags[itemNum] = True
        return
    

    def clearItemFlag(self, itemNum):
        self.itemflags[itemNum] = False
        return

    
    def getItemWeight(self, itemNum):
        return self.items[itemNum].getWeight()
    
   
    def getItemValue(self, itemNum):
        return self.items[itemNum].getValue()


    def copy(self):
        instance = Instance(self.num_items, self.capacity, self.weight, self.value, self.items, self.itemflags)
        return instance
    