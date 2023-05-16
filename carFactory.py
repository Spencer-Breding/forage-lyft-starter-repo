# -*- coding: utf-8 -*-
"""
Created on Mon May 15 20:07:49 2023

@author: Spencer Breding
"""

from abc import ABC, abstractmethod
from car import Car
from datetime import datetime

class CarFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass
    
class create_calliope(CarFactory, current_date, last_service_date, current_mileage, last_service_mileage):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        
    def create_car(self):
        return Car(self.current_date, self.last_service_date, self.current_mileage, self.last_service_mileage)
    
class create_glissade(CarFactory, current_date, last_service_date, current_mileage, last_service_mileage):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        
    def create_car(self):
        return Car(self.current_date, self.last_service_date, self.current_mileage, self.last_service_mileage)

class create_palindrome(CarFactory, current_date, last_service_date, warning_light_on):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.warning_light_on = warning_light_on
        
    def create_car(self):
        return Car(self.current_date, self.last_service_date, self.warning_light_on)
    
class create_rorschach(CarFactory, current_date, last_service_date, current_mileage, last_service_mileage):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        
    def create_car(self):
        return Car(self.current_date, self.last_service_date, self.current_mileage, self.last_service_mileage)
    
class create_thovex(CarFactory, current_date, last_service_date, current_mileage, last_service_mileage):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        
    def create_car(self):
        return Car(self.current_date, self.last_service_date, self.current_mileage, self.last_service_mileage)
        