# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:34:56 2023

@author: Spencer
"""

from abc import ABC, abstractmethod

class Tire(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class CarriganTire(Tire):
    def __init__(self, tires):
        self.tires = tires
        
    def needs_service(self):
        return any(tire >= 0.9 for tire in tires)
    
class OctoprimeTire(Tire):
    def __init__(self, tires):
        self.tires = tires
        
    def needs_service(self):
        return sum(tires) >= 3