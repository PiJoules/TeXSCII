"""
Lexer class for parsing lines of LaTex.
"""

import Fraction
import Subscript
import Superscript
import Root

class Lexer(object):
	def __init__(self):
		self.commands = {
			"frac": Fraction.Fraction(),
			"_": Subscript.Subscript(),
			"^": Superscript.Superscript(),
			"root": Root.Root()
		}

	def parse_line(self, line):
		map_result = [""] # 2D array of characters
		max_line_len = 0
		zero_index = 0
		commands = [] # List of commands read in

		# Parse the line
		i = 0
		while i < len(line):
			c = line[i]
				
			# Commands can be single (ie. _,^) or multiple characters (\frac,\root)
			if c in self.commands or c == "\\":
				# Found a command. Filter which one it is
				command = ""
				j = 1
				if c == "\\":	
					while line[i+j] != "{":
						command += line[i+j]
						j += 1
				else:
					command = c
				commands.append(command)

				if command in self.commands:
					if line[i+j+1] == "}":
						print "Argument for command '" + command + "' not given"
						return

					argc = self.commands[command].argc
					args = [""]*argc
					for k in range(argc):
						bracket_count = 1 # Counter for counting bracket pairs
						j += 1 # Currently on the {. Move 1 to get the the arg.
						while bracket_count > 0:
							if line[i+j] == "{":
								bracket_count += 1
							elif line[i+j] == "}": # Break immediately on finding a } and finishing bracket pairs
								bracket_count -= 1
								if bracket_count <= 0:
									break

							# Actually keep track of the argument
							args[k] += line[i+j]
							j += 1
						j += 1 # Move another 1 to get onto the next char.

					"""
					IN THE EVENT OF A NESTED COMMAND, FIND THE MAP PRODUCED AND APPLY IT
					TO THIS CURRENT MAP
					"""
					# Cases for each command
					disp, disp_zero = self.commands[command].apply_args(args)

					# Apply the display
					# Add any new levels
					for k in range(0,disp_zero-zero_index):
						map_result.insert(0," "*max_line_len)
					for k in range(0,zero_index-disp_zero):
						map_result.append(" "*max_line_len)
					while len(map_result) < len(disp):
						map_result.append(" "*max_line_len)
					zero_index = max(zero_index,disp_zero)

					# Special cases
					if len(commands) > 1:
						# Specific case for _{a}^{b}
						if commands[-1] == "^" and commands[-2] == "_":
							k = 1
							# Keep moving back unti the bottom left char is not a whitespace char
							while map_result[zero_index-disp_zero+1][-k] == " ":
								map_result[zero_index-disp_zero] = map_result[zero_index-disp_zero][:-1]
								k += 1

						# Specific case for ^{a}_{b}
						if commands[-1] == "_" and commands[-2] == "^":
							k = 1
							# Keep moving back unti the bottom left char is not a whitespace char
							while map_result[zero_index-disp_zero][-k] == " ":
								map_result[zero_index-disp_zero+len(disp)-1] = map_result[zero_index-disp_zero+len(disp)-1][:-1]
								k += 1

					# Add the display content
					for k in range(len(disp)):
						map_result[k+(zero_index-disp_zero)] += disp[k]

					# Reset the length
					max_line_len = max([len(r) for r in map_result])

					# Append any necessary spaces
					for k in range(len(map_result)):
						while len(map_result[k]) < max_line_len:
							map_result[k] += " "

					i += j # Skip the command after reading it
					continue
			else:
				for j in range(len(map_result)):
					if j == zero_index:
						map_result[zero_index] += c
					else:
						map_result[j] += " "
				max_line_len += 1
			i += 1

		return [map_result, zero_index]

	def parse_and_print(self,line):
		print "\n".join(self.parse_line(line.strip())[0])
