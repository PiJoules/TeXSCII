"""
Implementation of TeXSCII
"""

import sys
import copy
from Lexer import Lexer


if __name__ == "__main__":
	lex = Lexer()
	for line in sys.stdin:
		lex.parse_and_print(line)
		print ""