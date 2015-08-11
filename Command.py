"""
Command class
"""

class Command(object):
	def __init__(self, argc):
		self.argc = argc

	"""
	Check whether or not a string contains (a command with) arguments.
	"""
	def line_has_args(self, line):
		for i in range(1, len(line)):
			# Have a { to indicate an argument. \{ may indicate a literal {, not a arg.
			if not line[i-1] == "\\" and line[i] == "{":
				return True
		return False