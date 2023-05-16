# -*- coding: utf-8 -*-
"""
Created on Mon May 15 23:02:30 2023

@author: Spencer Breding
"""

from battery import *
from engine import *

class Car():
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    
    def needs_service():
        return self.battery.needs_service() and self.engine.needs_service()
        