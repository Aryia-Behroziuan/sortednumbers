# -*- coding: utf-8 -*-
"""
Created on Mon May  6 06:21:15 2019

@author: Faradars-pc2
"""

import unittest
import datetime
import genetic

class SortedNumbersTests(unittest.TestCase):
    
    def test_sort_10_numbers(self):
        self.sort_numbers(10)
        
    def sort_numbers(self, totalNumbers):
        geneset = [i for i in range(100)]
        startTime = datetime.datetime.now()
        
        def fnDisplay(candidate):
            display(candidate, startTime)
            
        def fnGetFitness(genes):
            return get_fitness(genes)
        
        optimalFitness = Fitness(totalNumbers, 0)
        best = genetic.get_best(fnGetFitness, totalNumbers,
                                optimalFitness, geneset, fnDisplay)
        self.assertTrue(not optimalFitness > best.Fitness)
        
    def test_benchmark(self):
        genetic.Benchmark.run(lambda: self.sort_numbers(40))
        
        
class Fitness:
    NumbersInSequenceCount = None
    TotalGap = None

    def __init__(self, numbersInSequenceCount, totalGap):
        self.NumbersInSequenceCount = numbersInSequenceCount
        self.TotalGap = totalGap
        
    def __gt__(self, other):
        if self.NumbersInSequenceCount != other.NumbersInSequenceCount:
            return self.NumbersInSequenceCount > other.NumbersInSequenceCount
        return self.TotalGap < other.TotalGap
    
    def __str__(self):
        return "{0} Sequential, {1} Total Gap".format(
                self.NumbersInSequenceCount,
                self.TotalGap)
        
def get_fitness(genes):
    fitness = 1
    gap = 0
    for i in range(1, len(genes)):
        if genes[i] > genes[i -1]:
            fitness += 1
        else:
            gap += genes[i - 1] - genes[i]
    return Fitness(fitness, gap)        

def display(candidate, startTime):
    timeD = datetime.datetime.now() - startTime
    print("{0}\t=>{1}\t{2}".format(
            ', '.join(map(str, candidate.Genes)),
            candidate.Fitness,
            str(timeD)))
    
if __name__ == "__main__":
    unittest.main()    
    



















        
        