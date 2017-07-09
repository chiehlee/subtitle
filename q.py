#!/usr/bin/env python
# Chieh Lee Jun 2017

import os
import sys
import time
import re

def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

s = r'Dialogue: 0,0:47:14.27,0:47:16.59,Default,NTP,0,0,0,,{\fad(50,50)}aaa'

print displaymatch(re.match(r".*(.).*\1", '717az'))
m = re.search(r'(\d+):(\d{2}):(\d{2}\.\d{2})', s)
m2 = re.finditer(r'(\d+):(\d{2}):(\d{2}\.\d{2})', s)
for x in m2:
	print x.group()
print re.split(r'\w{8}', s)
print m.group()
print m.groups()
print m.start()
print m.end()
print m.span()
print s[12:22]
print 
time_pattern = re.compile(r'(\d+):(\d{2}):(\d{2}\.\d{2})')

ori_startline = '0:47:04.04'
tar_startline = '0:00:01.00'
ori_match = re.search(time_pattern, ori_startline)
tar_match = re.search(time_pattern, tar_startline)
ori_groups = ori_match.groups()
tar_groups = tar_match.groups()

def toms(timestamp):
	time_pattern = re.compile(r'(\d+):(\d{2}):(\d{2}\.\d{2})')
	m = re.search(time_pattern, timestamp)
	mgroups = m.groups()
	return int(float(mgroups[0]) * 3600000 + float(mgroups[1]) * 6000 + 
			float(mgroups[2]) * 1000)

print toms(ori_startline)
print toms(tar_startline)

ori_ms = '286040'
tar_ms = '1000'

def tots(ms):
	ms = int(ms)
	h = ms / 3600000
	m = (ms % 3600000) / 6000
	s = ((ms % 3600000) % 6000)
	return '%s:%s:%s.%s' % (str(int(h)), str(int(m)), str(s)[:2], str(s)[2:])

print tots(ori_ms)
print re.match(time_pattern, tots(ori_ms))
print tots(286040 - 285040)


	

print s
print re.match(r'^Dialogue', s).span()
m3 = re.finditer(r'(\d+):(\d{2}):(\d{2}\.\d{2})', s)
for x in m3:
	print x.span()
print re.findall(r'\d+:\d{2}:\d{2}\.\d{2}', s)
print re.sub(r'(\d+):(\d{2}):(\d{2}\.\d{2})', tots(286040 - 285040), s)