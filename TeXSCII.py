"""
https://www.reddit.com/r/dailyprogrammer/comments/38nhgx/20150605_challenge_217_practical_exercise_texscii/

You'll be given a LaTeX equation on one line. The commands you need to support are:
\frac{top}{bottom}: A fraction with the given top and bottom pieces
\sqrt{content}: A square-root sign
\root{power}{content}: A root sign with an arbitrary power (eg. cube-root, where the power 3 is at the top-left of the radical symbol)
_{sub}: Subscript
^{sup}: Superscript
_{sub}^{sup}: Subscript and superscript (one on top of the other)
\pi: Output the greek symbol for pi
Feel free to extend your solution to support any additional structures such as integral signs.


frac - at least 3 lines (1 for numerator, denominator, and line)
	 - line width is max width of either numerator or denominator

sqrt - at least 2 lines (1 for content, 1 for root top)
	 - width is 1 for the initial root, n-1 diagnol lines where n is the hight of the content, and m horizontal lines where m is the width of the content

root - at least 2 lines (1 for content, 1 for root top and power)
	 - width is 1 for the initial root, n-1 diagnol lines where n is the hight of the content, and m horizontal lines where m is the width of the content
	 - the power goes above the last diagnol line and before the first horizontal line

sub - starts on immediate bottom right of last character in the base

sup - starts on immediate top right of last character in the base

pi - output pi

"""


import sys
import copy

commands = {
	"frac": {
		"argc": 2,
		"disp": lambda args: [
			substitute_args("$0", args),
			"-"*max([len(arg) for arg in args]),
			substitute_args("$1", args)
		]
	}
}


"""
Substitute the arguments into how it will be displayed.
"""
def substitute_args(disp, args):
	for i in range(len(args)):
		disp = disp.replace("$"+str(i), args[i])
	return disp


"""
Check whether or not a string contains (a command with) arguments.
"""
def command_with_args(line):
	for i in range(1, len(line)):
		# Have a { to indicate an argument. \{ may indicate a literal {, not a arg.
		if not line[i-1] == "\\" and line[i] == "{":
			return True
	return False


def frac_map(args):
	disp = [
		"$0",
		"-",
		"$1"
	]
	zero_index = 1
	arg0_has_args = command_with_args(args[0])
	arg1_has_args = command_with_args(args[1])

	if arg0_has_args:
		sub_map, sub_map_zero = parse_pattern(args[0])

		# Replace the line with the new map
		del disp[0]
		for line in sub_map[::-1]:
			disp.insert(0,line)

		zero_index += sub_map_zero-1 # Adjust the zero index
	else:
		disp[0] = disp[0].replace("$0", args[0])

	if arg1_has_args:
		sub_map, sub_map_zero = parse_pattern(args[1])

		# Replace the line with the new map
		del disp[-1]
		for line in sub_map:
			disp.append(line)

		zero_index += sub_map_zero-1 # Adjust the zero index
	else:
		disp[-1] = disp[-1].replace("$1", args[1])

	disp[zero_index] = disp[zero_index]*max([len(x) for x in disp])

	return [disp, zero_index]


"""
Given a map with commands in any of its lines,
decide the commands, apply it to the map, and
decode them.
"""
def parse_map(initial_map, zero_index):
	max_line_len = max([len(x) for x in initial_map])
	i = 0
	while i < len(initial_map):
		line = initial_map[i]
		sub_map, sub_map_zero = parse_pattern(line)

		# Replace the line with the new map
		del initial_map[zero_index]
		for line in sub_map[::-1]:
			initial_map.insert(zero_index,line)

		zero_index += sub_map_zero-1 # Adjust the zero index
		i += 1
	return initial_map


def parse_pattern(line):
	map_result = [""] # 2D array of characters
	max_line_len = 0
	zero_index = 0

	# Parse the line
	i = 0
	while i < len(line):
		c = line[i]

		if c == "\\":
			# Found a command. Filter which one it is
			frac_start = i
			command = ""
			j = 1
			while line[i+j] != "{":
				command += line[i+j]
				j += 1

			if command in commands:
				if line[i+j+1] == "}":
					print "Argument for command '" + command + "' not given"
					return

				argc = commands[command]["argc"]
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
				disp, disp_zero = frac_map(args)

				# Apply the display
				# Add any new levels
				while len(map_result) < len(disp):
					if (len(disp)-len(map_result)) % 2 == 1:
						map_result.append(" "*max_line_len)
					else:
						map_result.insert(0," "*max_line_len)
						zero_index += 1 # Move the zero index

				# Add the display content
				for k in range(len(disp)):
					map_result[k] += disp[k]

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


if __name__ == "__main__":
	for line in sys.stdin:
		print "\n".join(parse_pattern(line.strip())[0])