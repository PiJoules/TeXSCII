"""
Root object

Format:

"""

import Lexer
from Command import Command

class Root(Command):
	def __init__(self):
		super(self.__class__, self).__init__(2)

	def apply_args(self,args):
		disp = [
			"$0_",
			" /",
			"v$1" # Content starts directly under the first underscore, not imediately after the v
		]
		zero_index = 2
		arg0_has_args = self.line_has_args(args[0])
		arg1_has_args = self.line_has_args(args[1])

		# The power
		power_len = 1
		if arg0_has_args:
			sub_map, sub_map_zero = Lexer.Lexer().parse_line(args[0])

			# Replace the line with the new map
			del disp[0]
			for line in sub_map[::-1]:
				disp.insert(0,line)

			for i in range(len(disp)-3):
				disp[i] += " "
			disp[-3] += "_"

			zero_index += len(disp)-1 # Adjust the zero index

			# Add space to account for the length of the first arg
			max_line_len = max([len(disp[i])-1 for i in range(len(disp)-2)])
			power_len = max_line_len
			for i in range(max_line_len-1):
				disp[-1] = " " + disp[-1]
				disp[-2] = " " + disp[-2]
		else:
			disp[0] = disp[0].replace("$0", args[0])
			power_len = len(disp[0])-1

			# Add space to account for the length of the first arg
			for i in range(len(disp[0])-2):
				disp[1] = " " + disp[1]
				disp[2] = " " + disp[2]

		# The content
		if arg1_has_args:
			sub_map, sub_map_zero = Lexer.Lexer().parse_line(args[1])

			# Replace the line with the new map
			del disp[-1]
			for line in sub_map:
				disp.append(line)
		else:
			del disp[-2] # No need for the diagnol for content of height 1
			zero_index -= 1
			disp[-1] = disp[-1].replace("$1", args[1])

			# Adjust the number of underscores on the above line and spaces on any further lines
			for j in range(len(disp)-2):
				disp[j] += " "*(len(disp[-1])-2)
			disp[-2] += "_"*(len(disp[-1])-2-(power_len-1))

		return [disp, zero_index]