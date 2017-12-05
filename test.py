#!/usr/bin/env python
# Chieh Lee Jun 2017
# -*- coding: utf-16 -*-
import urllib2
import urllib
import codecs
import sys

def printx(s):
	k = ''.join(format(ord(x), '02x') for x in s)
	count = 0
	p = '\\u'
	for y in k:
		p = p + y
		count = count + 1
		if count == 4:
			count = 0
			p = p + ' \\u'

	print p

f = open("[SFEO-Raws] Dragon Ball Super - 01 (BD 1080P x264 FLAC).ass", 'rb')
f2 = open('qq.ass', 'rb')
t = open('test.ass', 'wb+')
#t = open('test.ass')

for line in f:
	t.write(line)


#s3 = urllib.urlencode({'key2':s[:-1]}, True)

kkkkkk
eeee

u = f2.readline()
st = '\x3b\x00\x20\x00\x2f\x00\x2f\x00\x20\x00\x64\x6b\x57\x5b\x55\x5e'.decode('utf-16')
st2 = '\xa0\x4f\x9f\x53'
#print st
#print st2
#print u.encode('gb2312', 'ignore')

#print ' '.join(format(ord(x), '02x') for x in uu)




