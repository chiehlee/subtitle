#!/usr/bin/env python
# -*- coding: utf8 -*-
# Chieh Lee Jun 2017
import codecs
import os
import sys
import re


w = open('Hunter X Hunter 2011 - EP052 [BD 1920x1080 23.976fps AVC-yuv444p10 FLAC Chap] v2 - mawen1250.maplesnow.ass', 'rb')

r = w.read()
k = open('test.ass', 'wb+')
k.write(' '.join(format(ord(x), '#02x') for x in r))


master