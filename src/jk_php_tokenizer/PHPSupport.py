


import re



class PHPSupport(object):

	_REPL1 = {
		"n": "\n",
		"r": "\r",
		"t": "\t",
		"v": "\v",
		"e": "\x1B",
		"f": "\f",
	}

	_REPL2 = {
		"\x00": "\\0",
		"\x01": "\\x01",
		"\x02": "\\x02",
		"\x03": "\\x03",
		"\x04": "\\x04",
		"\x05": "\\x05",
		"\x06": "\\x06",
		"\x07": "\\x07",
		"\x08": "\\x08",
		"\t": "\\t",		# 0x09
		"\n": "\\n",		# 0x0a
		"\v": "\\v",		# 0x0b
		"\f": "\\f",		# 0x0c
		"\r": "\\r",		# 0x0d
		"\x0e": "\\x0e",
		"\x0f": "\\x0f",
		"\x10": "\\x10",
		"\x11": "\\x11",
		"\x12": "\\x12",
		"\x13": "\\x13",
		"\x14": "\\x14",
		"\x15": "\\x15",
		"\x16": "\\x16",
		"\x17": "\\x17",
		"\x18": "\\x18",
		"\x19": "\\x19",
		"\x1a": "\\x1a",
		"\x1b": "\\e",
		"\x1c": "\\x1c",
		"\x1d": "\\x1d",
		"\x1e": "\\x1e",
		"\x1f": "\\x1f",
		"\"": "\\\"",
		"\\": "\\\\",
	}

	_RE_OCTAL = re.compile("[0-7]{1,3}")
	_RE_HEX = re.compile("x[0-9A-Fa-f]{1,2}")
	_RE_UNICODE = re.compile("u{[0-9A-Fa-f]+}")

	#
	# Creates a text from a given string that directly could be inserted into a PHPSupport source code file to represent a string.
	#
	@staticmethod
	def encodeString(someString):
		ret = ""
		for c in someString:
			ret += PHPSupport._REPL2.get(c, c)
		return ret
	#

	#
	# Parses (= decodes) a PHPSupport source code string.
	#
	# See: http://php.net/manual/en/language.types.string.php
	#
	@staticmethod
	def decodeString(someString):
		ret = ""
		bMasked = False
		i = 0
		imax = len(someString)
		while i < imax:
			c = someString[i]
			if bMasked:
				result = PHPSupport._RE_UNICODE.match(someString, i)
				if result:
					clip = someString[i:result.endpos()]
					i += len(clip)
					ret += chr(int(clip))
				else:
					result = PHPSupport._RE_HEX.match(someString, i)
					if result:
						clip = someString[i:result.endpos()]
						i += len(clip)
						if len(clip) == 1:
							clip = "0" + clip
						ret += chr(int(clip, 16))
					else:
						result = PHPSupport._RE_OCTAL.match(someString, i)
						if result:
							clip = someString[i:result.endpos()]
							i += len(clip)
							while len(clip) < 3:
								clip = "0" + clip
							ret += chr(int(clip, 8))
						else:
							# fallback
							repl = PHPSupport._REPL1.get(c, None)
							if repl is None:
								ret += c
							else:
								ret += repl
							i += 1
				bMasked = False
			else:
				if c == "\\":
					bMasked = True
				else:
					ret += c
				i += 1
		return ret
	#

#





