#!/usr/bin/python3
import sys

# Someone is using a cipher that maps the alphabet to the reversed alphabet,
# meaning a -> z, b -> y, c -> x and so on.  This has the fortunate property
# of being it's own inverse.  Using this algorithm will encipher text, or if
# applied to enciphered text, will decipher it.
#
# Example usage: ./reverse.py "Svool, dliow"
#
# Produces the result: "Hello, world"

# Build map for translation
chars = 'abcdefghijklmnopqrstuvwxyz'
rev_chars = chars[::-1] + chars.upper()[::-1]
chars = chars + chars.upper()
char_map = ''.maketrans(chars, rev_chars)

# Translate and print result
print(' '.join(sys.argv[1:]).translate(char_map))

