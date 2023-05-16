# -*- coding: utf-8 -*-
"""
Created on Mon May 15 23:02:30 2023

@author: Spencer Breding
"""

from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    
    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
        