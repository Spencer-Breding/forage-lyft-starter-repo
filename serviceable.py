# -*- coding: utf-8 -*-
"""
Created on Mon May 15 23:07:09 2023

@author: Spencer Breding
"""

from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass