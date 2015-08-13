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
			" /", # This will actually be deleted, but is here for visualization
			"v$1" # Content starts directly under the first underscore, not imediately after the v
		]
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
			for i in range(power_len-1):
				disp[-1] = " " + disp[-1]
				disp[-2] = " " + disp[-2]

		# The content
		if arg1_has_args:
			sub_map, sub_map_zero = Lexer.Lexer().parse_line(args[1])

			# Add the diagnols
			del disp[-2]
			h = len(sub_map)
			for i in range(h-1):
				disp.insert(-1-i, " "*(power_len+i) + "/")
				while (len(disp[-2-i]) < h+power_len-1):
					disp[-2-i] += " "

			# Add the sub_map to the last h rows now
			for i in range(h):
				disp[-h+i] += sub_map[i]

			# Adjust the upper rows
			if h > power_len:
				disp[-1] = disp[-1].replace("$1", " "*(h-1))
				for i in range(len(disp)-h):
					disp[i] = " "*(h-1) + disp[i]
			else:
				for i in range(h):
					disp[-1-i] = disp[-1-i].replace("$1", " "*(h-1))[(h-1):]
			disp[-h-1] += "_"*(max([len(l) for l in sub_map])-1)
		else:
			del disp[-2] # No need for the diagnol for content of height 1
			disp[-1] = disp[-1].replace("$1", args[1])

			# Adjust the number of underscores on the above line and spaces on any further lines
			for j in range(len(disp)-2):
				disp[j] += " "*(len(disp[-1])-2)
			disp[-2] += "_"*(len(disp[-1])-2-(power_len-1))

		# Trim leading whitespace
		while all([x[0] == " " for x in disp]):
			for i in range(len(disp)):
				disp[i] = disp[i][1:]

		return [disp, len(disp)-1]