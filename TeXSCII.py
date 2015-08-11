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
from Lexer import Lexer


if __name__ == "__main__":
	lex = Lexer()
	for line in sys.stdin:
		lex.parse_and_print(line)
		print ""