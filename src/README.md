jk_php_tokenizer
==========

Introduction
------------

This python module is a tokenizer for configuration files written in PHP.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/....)
* [pypi.python.org](https://pypi.python.org/pypi/jk_php_tokenizer)

Why this module?
----------------

Quite some web applications store their configuration data in PHP files. While this is convenient for the web application developers this has a problematic drawback: If for some reason this configuration needs to be processed (e.g. if you want to do a backup) this is a problem as this configuration data can not be read easily.

This module helps moving towards building a parser for these files by providing a ready to use PHP tokenizer.

Limitations of this module
--------------------------

This module only performs tokenization, not parsing.

As it is intended for reading PHP configuration files it has not been extensively been tested with files other than configuration files.

How to use this module
----------------------

### Import this module

Please include this module into your application using the following code:

```python
import jk_php_tokenizer
```

### Tokenize a file

Tokenizing is easy. The next lines show how to use the tokenizer:

```python
PATH_OF_PHP_FILE = "..."

tokenizer = jk_php_tokenizer.PHPTokenizer()

with open(PATH_OF_PHP_FILE, "r") as f:
	for token in tokenizer.tokenize(f.read()):
		print(token)
```

### The token data structure

A token is a `jk_utils.Token` data structure. It has the following fields:

* `type` - the type of the token
* `value` - the token text
* `lineNo` - the line number where the token begins
* `colNo` - the colum number where the token begins

### Token types

The following types of tokens are provided by the tokenizer:

* `int`
* `str1`
* `str2`
* `bool`
* `null`
* `comment`
* `phpintro`
* `phpoutro`
* `varref`
* `commentx`
* `lparen1`
* `rparen1`
* `lparen2`
* `rparen2`
* `lparen3`
* `rparen3`
* `bool`
* `word`
* `op`
* `SPACE`
* `NEWLINE`
* `semicolon`

Contact Information
-------------------

This work is Open Source. This enables you to use this work for free.

Please have in mind this also enables you to contribute. We, the subspecies of software developers, can create great things. But the more collaborate, the more fantastic these things can become. Therefore Feel free to contact the author(s) listed below, either for giving feedback, providing comments, hints, indicate possible collaborations, ideas, improvements. Or maybe for "only" reporting some bugs:

* Jürgen Knauth: jknauth@uni-goettingen.de, pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



