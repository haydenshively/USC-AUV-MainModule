from ..strategy import Strategy as AbstractStrategy
from .test import TestA, TestB

def list_of_strategies(also_return_names = False):
    if also_return_names: return ((TestA, TestA.name), (TestB, TestB.name))
    else: return (TestA, TestB)

def initialize(Strategy, gyro, odometer):# TODO use this issubclass pattern everywhere
    if issubclass(Strategy, AbstractStrategy): return Strategy(gyro, odometer)
    else: raise ValueError('Cannot initialize non-Strategy class as a Strategy')