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
def contains_args(line):
	for i in range(1, len(line)):
		# Have a { to indicate an argument. \{ may indicate a literal {, not a arg.
		if not line[i-1] == "\\" and line[i] == "{":
			return True
	return False


"""
Given a map with commands in any of its lines,
decide the commands, apply it to the map, and
decode them.
"""
def parse_map(initial_map):
	pass


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
				bracket_count = 1 # Counter for counting bracket pairs
				for k in range(argc):
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
					if contains_args(args[k]):
						args[k] = parse_pattern(args[k]) # The argument is now a map instead of a string

				# Cases for each command
				disp = commands[command]["disp"](args)

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

	return map_result


"""
Parse the line.
"""
def parse_line(line):
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
					j += 1 # Currently on the {. Move 1 to get the the arg.
					while line[i+j] != "}":
						args[k] += line[i+j]
						j += 1
					j += 1 # Move another 1 to get onto the next char.

				# Cases for each command
				disp = commands[command]["disp"](args)

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
				print "command '" + command + "' does not exist"
				return
		else:
			for j in range(len(map_result)):
				if j == zero_index:
					map_result[zero_index] += c
				else:
					map_result[j] += " "
			max_line_len += 1
		i += 1

	print "\n".join(map_result)
	print ""

if __name__ == "__main__":
	for line in sys.stdin:
		parse_line(line.strip())