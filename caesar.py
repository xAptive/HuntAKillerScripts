#!/usr/bin/python3

# Someone is using a Caesar cipher variant where only every nth letter is
# enciphered.  Enciphered text is actually tagged with all the needed
# information to decipher it, once you understand the algorithm.  Text might
# begin with a marking like 2/6.  The first number tells you how often the
# cipher is applied, and the second number tells you by how much it is shifted.
#
# For example, consider the the follwing ciphertext:
#
# 2/4 Hilpo, aovlh
#
# That tells you every other letter is enciphered, and that it's using a shift
# cipher by 4.  To decipher that text with this script, run the following
# command:
#
# ./caesar.py 2 -4 "Hilpo, aovlh"
#
# That means encipher every other character, and shift back 4, and produces the
# text "Hello, world"

import sys

# Get settings
skip = int(sys.argv[1])
shift = int(sys.argv[2])

# Build map for translation
chars = 'abcdefghijklmnopqrstuvwxyz'
map_chars = ''.join([chr(((ord(char) - 97 + shift) % 26) + 97) for char in chars])
chars = chars + chars.upper()
map_chars = map_chars + map_chars.upper()
char_map = ''.maketrans(chars, map_chars)

# Translate and print result
results = []
for idx, char in enumerate(' '.join(sys.argv[3:])):
    if (idx + 1) % skip == 0:
        results.append(char.translate(char_map))
    else:
        results.append(char)
print(''.join(results))

