# -*- coding: utf-8 -*-
"""
Created on Mon May 15 20:11:14 2023

@author: Spencer Breding
"""

from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass
    
class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
    
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
    
class SternmanEngine(Engine):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on
    
    def needs_service(self):
        return self.warning_light_on
    
class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
    
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000