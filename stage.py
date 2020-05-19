#!/usr/bin/python3

# Someone is using stage location (upper left, center stage, etc.) as a code
# to hide text.  Ciphertext is written as such: UL3, SC1, LR2, etc.).  There is
# a key that goes along with each of these ciphertexts, which tells you all you
# need to know to cipher it.  Each set of three letters maps to 3x3 box.  A key
# might look like this:
#
#    |   |def
#------------
#    |   |
#------------
#    |   |
#
# You can use this knowledge to sequentially fill in the rest of the box like 
# so:
#
# yz |abc|def
#------------
# ghi|jkl|mno
#------------
# pqr|stu|vwx
#
# The stage directions map as such:
#
# UR |UC |UL
#------------
# SR |SC |SL
#------------
# DR |DC |DL
#
# And so therefore, in this case, the code SC2 would refer to the letter "k", 
# because SC refers to the center box, the center box has the letters jkl, and
# 2 means the second letter in that box, or "k"
#
# To use this script, input the location of the key, and the letters in the key:
# For example:
#
# ./stage.py UL def "SR2 UL2 SC3 SC3 SL3 DL2 SL3 DR3 SC3 UL1"
#
# Produces: "helloworld"
   
import sys

# Initial setup
char_locs = ['UR', 'UC', 'UL', 'SR', 'SC', 'SL', 'DR', 'DC', 'DL']
sets = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']

# Get configuration
key_loc = sys.argv[1].upper()
key_set = sys.argv[2].lower()

# Determine offsets based on configuration
map_start = char_locs.index(key_loc)
set_start = sets.index(key_set)

# Fill in character map
char_map = [sets[(i + set_start - map_start) % 9] for i in range(9)]

# Normalize input (Handle individual args or args that came in as a string)
items = []
for x in sys.argv[3:]:
    items.extend(x.split(' '))

results = []
# Do translation
for item in items:
    loc = char_locs.index(item[0:2])
    idx = int(item[2]) - 1
    results.append(char_map[loc][idx])

# Show result
print(''.join(results))
