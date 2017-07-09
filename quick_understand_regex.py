#!/usr/bin/env python
# Chieh Lee Jun 2017

import os
import sys
import time
import re

s = 'Dialogue: 0,0:54:32.20,0:54:32.82,Default,NTP,0,0,0,,{fad(50,50)}'

def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

print displaymatch(re.match(r".*(.).*\1", '717az'))
m = re.match(r'(\w{8}).*(\w{7})', s)
m2 = re.finditer(r'(\w{8})', s)
for x in m2:
	print x.group()
print re.split(r'\w{8}', s)
print m.group()
print m.groups()
print m.start()
print m.end()
print m.span()
