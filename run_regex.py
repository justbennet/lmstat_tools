#!/usr/bin/env python3

import re
import regex   # Assumed to be in the same directory as this script

# Example data
matlab = '    grundoon node3447.your.computer.ex /dev/tty (v46) (flux-license1.miserver.it.umich.edu/1709 317905), start Sat 9/16 3:15'
abaqus = '    grundoon node3152.your.computer.ex /dev/tty (v62.5) (flux-license1.miserver.it.umich.edu/27000 3680), start Tue 9/12 4:52, 36 licenses'

# Parse the matlab data using a regex
m = regex.get_matlab(matlab)
a = regex.get_abaqus(abaqus)

# Translate matched expressions into a dict
print("\nMatlab license information as dict")
print(m.groupdict(m), '\n')

print("\nAbaqus license information as dict")
print(a.groupdict(a), '\n')

