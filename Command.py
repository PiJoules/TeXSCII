"""
Abstract Command class to be implemented by the actual commands
"""

import abc
 
class Command():
    __metaclass__  = abc.ABCMeta
 
    @abc.abstractmethod
    def to_strings(self):
    	pass

    @abc.abstractmethod
    def set_x(self, x):
    	pass

    @abc.abstractmethod
    def get_x(self):
    	pass

    @abc.abstractmethod
    def get_children(self):
    	pass