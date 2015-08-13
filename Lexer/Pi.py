"""
Pi object

Just print pi
"""

import Lexer
from Command import Command

class Pi(Command):
	def __init__(self):
		super(self.__class__, self).__init__(0)

	def apply_args(self,args):
		return [u"\u03c0", 0]