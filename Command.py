import abc
 
class Command():
    __metaclass__  = abc.ABCMeta
 
    @abc.abstractmethod
    def to_string(self):
         """Returns the string representation of this command"""