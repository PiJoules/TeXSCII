from Command import Command

class Frac(Command):
	def __init__(self, x, y, num, den):
		self.x = x
		self.y = y
		self.lines = [num,'-',den]

	def to_strings(self):
		string_lines = [0]*3
		num = self.lines[0]
		den = self.lines[2]
		string_lines[0] = num
		string_lines[1] = '-'*max(len(num), len(den))
		string_lines[2] = den
		return string_lines

	def get_x(self):
		return self.x

	def set_x(self, x):
		self.x = x

	def get_children(self):
		pass