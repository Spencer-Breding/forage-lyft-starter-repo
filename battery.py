# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:12:27 2023

@author: Spencer Breding
"""

from abc import ABC, abstractmethod

class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self):
        time_since_last_service = self.current_date - self.last_service_date
        return time_since_last_service.years >= 4
    
class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self):
        time_since_last_service = self.current_date - self.last_service_date
        return time_since_last_service.years >= 2