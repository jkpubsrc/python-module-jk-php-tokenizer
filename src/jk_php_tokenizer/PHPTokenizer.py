


import re
import os
import sys





from jk_utils.tokenizer import RegExBasedTokenizer, Token

from .PHPSupport import PHPSupport











#
# This tokenizer parses a PHPSupport file.
#
class PHPTokenizer(RegExBasedTokenizer):

	def __init__(self):
		super().__init__([
			( "phpintro", "<\\?php" ),
			( "phpoutro", "\\?>" ),
			( "str1", r"'", r"[^']*", r"'" ),
			( "str2", r"\"", r"[^\"]*", r"\"" ),
			( "int_1", r"[+-]?[1-9][0-9]*" ),
			( "int_2", r"0" ),
			( "varref", r"\$", r"[a-zA-Z_][a-zA-Z0-9_]*", None ),
			( "commentx", "#=#" ),
			( "comment_1", "#[^\n]*" ),
			( "comment_2", "//[^\n]*" ),
			( "comment_3", "/*[.*?]*/" ),
			( "lparen1", "\\(" ),
			( "rparen1", "\\)" ),
			( "lparen2", "\\[" ),
			( "rparen2", "\\]" ),
			( "lparen3", "\\{" ),
			( "rparen3", "\\}" ),
			( "semicolon", r";" ),
			( "bool_1", r"true" ),
			( "bool_2", r"false" ),
			( "null", r"null" ),
			( "word", r"[a-zA-Z_][a-zA-Z0-9_]*" ),
		])

		i = 1
		for op in [ "===", "!==", "<<=", ">>=", "<=>",
			"<>", "||", "&&", "==", "!=", "+=", "-=", "*=", "/=", "%=", "<=", ">=", "^=", "=>", "++", "--", ">>", "<<", "??", "->",
			"^", "!", "%", "+", "-", "*", "/", ".", ",", "?", ":", "~", "@", "&", "|", "=" ]:
			self.addTokenPattern("op_" + str(i), re.escape(op))
			i += 1

		self.compile()

		self.registerTypeParsingDelegate("int", "1", self.__parseInt)
		self.registerTypeParsingDelegate("int", "2", self.__parseInt)
		self.registerTypeParsingDelegate("str1", None, PHPSupport.decodeString)
		self.registerTypeParsingDelegate("str2", None, PHPSupport.decodeString)
		self.registerTypeParsingDelegate("bool", "1", self.__parseBool)
		self.registerTypeParsingDelegate("bool", "2", self.__parseBool)
		self.registerTypeParsingDelegate("null", None, self.__parseNull)
	#

	def __parseNull(self, rawTokenText):
		return None
	#

	def __parseBool(self, rawTokenText):
		return rawTokenText == "true"
	#

	def __parseInt(self, rawTokenText):
		return int(rawTokenText)
	#

	def tokenize(self, text, bEmitWhiteSpaces = False, bEmitNewLines = False, bEmitComments = False):
		for token in super().tokenize(text, bEmitWhiteSpaces, bEmitNewLines):
			if (token.type == "comment") and not bEmitComments:
				continue
			yield token
	#

#









