"""
Superscript object

Format:
 2
x
"""

import Lexer
from Command import Command

class Superscript(Command):
	def __init__(self):
		super(self.__class__, self).__init__(1)

	def apply_args(self,args):
		disp = [
			"$0",
			"" # Zero
		]
		zero_index = 1
		arg0_has_args = self.line_has_args(args[0])

		if arg0_has_args:
			sub_map, sub_map_zero = Lexer.Lexer().parse_line(args[0])

			# Replace the line with the new map
			del disp[0]
			for line in sub_map[::-1]:
				disp.insert(0,line)

			zero_index += len(sub_map)-1 # Adjust the zero index
		else:
			disp[0] = disp[0].replace("$0", args[0])

		return [disp, zero_index]