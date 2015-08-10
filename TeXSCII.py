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


Classes
- Command
  - class that will take place of any of the commands listed above
  - the class can have children representing the content of it as either a string or another Command
  - will have a to_string() function that converts a Command object and all nested Command objects to a string
  - the to_strings() functions will vary depending on what kind of command it actually is
"""


import sys

commands = {
	"frac": {
		"argc": 2,
		"disp": "$0/$1" # arg0 / arg1
	}
}

def substitute_args(disp, args):
	for i in range(len(args)):
		disp = disp.replace("$"+str(i), args[i])
	return disp

def parse_line(line):
	# Parse the line
	result = ""
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
				result += substitute_args(commands[command]["disp"], args)
				i += j # Skip the command after reading it
				continue
			else:
				print "command '" + command + "' does not exist"
				return
		else:
			result += c
		i += 1

	print result

if __name__ == "__main__":
	for line in sys.stdin:
		parse_line(line)