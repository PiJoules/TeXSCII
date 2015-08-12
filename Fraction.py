"""
Fraction object

Format:
$0
--
$1
"""

import Lexer
from Command import Command

class Fraction(Command):
	def __init__(self):
		super(self.__class__, self).__init__(2)

	def apply_args(self,args):
		disp = [
			"$0",
			"-", # Zero
			"$1"
		]
		zero_index = 1
		arg0_has_args = self.line_has_args(args[0])
		arg1_has_args = self.line_has_args(args[1])

		if arg0_has_args:
			sub_map, sub_map_zero = Lexer.Lexer().parse_line(args[0])

			# Replace the line with the new map
			del disp[0]
			for line in sub_map[::-1]:
				disp.insert(0,line)

			zero_index += len(sub_map)-1 # Adjust the zero index
		else:
			disp[0] = disp[0].replace("$0", args[0])

		if arg1_has_args:
			sub_map, sub_map_zero = Lexer.Lexer().parse_line(args[1])

			# Replace the line with the new map
			del disp[-1]
			for line in sub_map:
				disp.append(line)
		else:
			disp[-1] = disp[-1].replace("$1", args[1])

		disp[zero_index] = disp[zero_index]*max([len(x) for x in disp])

		return [disp, zero_index]