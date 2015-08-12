"""
Subscript object

Format:
log (x)
   2
"""

import Lexer
from Command import Command

class Subscript(Command):
	def __init__(self):
		super(self.__class__, self).__init__(1)

	def apply_args(self,args):
		disp = [
			" ", # Zero
			"$0"
		]
		zero_index = 0
		arg0_has_args = self.line_has_args(args[0])

		if arg0_has_args:
			sub_map, sub_map_zero = Lexer.Lexer().parse_line(args[0])

			# Replace the line with the new map
			del disp[-1]
			for line in sub_map:
				disp.append(line)
		else:
			disp[-1] = disp[-1].replace("$0", args[0])

		disp[zero_index] = disp[zero_index]*max([len(x) for x in disp])

		return [disp, zero_index]