#!/usr/bin/python
# -*- coding: utf8 -*-
# Chieh Lee Jun 2017

import codecs
import os
import sys
import re

# handle 1 subtitle file (object) at a time
class subtitle:

	print '\nHello! Chieh Lee made this piece :)\n'
	print 'here is something important about this piece:'
	print ' - currently only accept encoding UTF-8'
	print ' - other endocing may result garbled characters\n'

	# constructor
	def __init__(self):
		outputfile = ''
		ori_startline = ''
		tar_startline = ''
		file_type = ''

	# type check sys.argv[1] to be ".ass" file
	# if tyep not expected, print str and exit(0)
	try:
		if os.path.isfile(sys.argv[1]) and \
			os.path.basename(sys.argv[1])[-4:] == '.ass':
			subfile = open(sys.argv[1], 'rb')
			file_type = '.ass'
		elif os.path.isfile(sys.argv[1]) and \
			os.path.basename(sys.argv[1])[-4:] == '.ssa':
			subfile = open(sys.argv[1], 'rb')
			file_type = '.ssa'
		else:
			print 'Bad Path, Try again!'
			exit(0)
	except IndexError as e:
		print 'Index Error, Bad Path'
		exit(1)

	global ts_pattern
	ts_pattern = re.compile(r'(\d+):(\d{2}):(\d{2}\.\d{2})')
		
	# this method set the desired starting event line for change
	# by giving the corresponding timestamp
	def set_ori_startline(self):
		self.ori_startline = raw_input('Initial event line to be changed ' +
									'from original .ass or .ssa file ' + 
									'(0:00:00.00 format):')
		if self.ori_startline == '000': # hidden code to exit 
			exit(0)
		elif re.match(ts_pattern, self.ori_startline) == None:
			print 'Bad event line Format please try again.'
			self.set_ori_startline()

	# this method set the target timestamp for revision
	def set_tar_startline(self):
		self.tar_startline = raw_input('Target time to change for the first ' +
									'event lines (0:00:00.00 format):')
		if self.tar_startline == '000':
			exit(0)
		elif re.match(ts_pattern, self.tar_startline) == None:
			print 'Bad event line Format please try again.'
			self.set_tar_startline()

	# create new output file in binary mode and static attribute for the file
	def create_newfile(self):
		if os.path.exists('new_output.ass'):
			# create ascending order file number if duplicated
			for x in xrange(9999):
				if not os.path.exists('new_output(%s).ass' % str(x + 1)):
					self.outputfile = open('new_output(%s).ass' % str(x + 1), 'wb+')
					break
		else:
			self.outputfile = open('new_output.ass', 'wb+')

		# create new output file in binary mode and static attribute for the file
	def create_newfile_ssa(self):
		if os.path.exists('new_output.ssa'):
			# create ascending order file number if duplicated
			for x in xrange(9999):
				if not os.path.exists('new_output(%s).ssa' % str(x + 1)):
					self.outputfile = open('new_output(%s).ssa' % str(x + 1), 'wb+')
					break
		else:
			self.outputfile = open('new_output.ssa', 'wb+')

	# convert timestamp to mileseconds return as int
	@staticmethod
	def toms(timestamp):
		m = re.search(ts_pattern, timestamp)
		mgroups = m.groups()
		return int(float(mgroups[0]) * 3600000 + float(mgroups[1]) * 60000 +
					float(mgroups[2]) * 1000)
	
	# convert mileseconds to timestamp return as str
	@staticmethod
	def tots(ms):
		ms = int(ms)
		# hour
		h = ms / 3600000
		# minute
		m = (ms % 3600000) / 60000
		# secode
		s = ((ms % 3600000) % 60000) / 1000
		# milesecond - get rid of the last decimal 
		# point because of the .ass/.ssa format
		ss = (((ms % 3600000) % 60000) % 1000) / 10
		return '{}:{:02}:{:02}.{:02}'.format(h, m, s, ss)

	# return difference between two timestamps as milesecond
	def difference(self):
		return self.toms(self.ori_startline) - self.toms(self.tar_startline)

	# return revised event line with new timestamp
	def revise_event(self, line):
		matches = re.findall(r'\d+:\d{2}:\d{2}\.\d{2}', line)
		new_start = self.tots(self.toms(matches[0]) - self.difference())
		new_end   = self.tots(self.toms(matches[1]) - self.difference())
		line = line.replace(matches[0], new_start)
		line = line.replace(matches[1], new_end)
		return line

	# for test only please ignore: print encode in hex
	@staticmethod
	def printx(s):
		k = ''.join(format(ord(x), '02x') for x in s)
		count = 0
		p = '\\u'
		for y in k:
			p = p + y
			count = count + 1
			if count == 2:
				count = 0
				p = p + ' \\u'

		return p

	# for test only please ignore: print encode in hex
	@staticmethod
	def printb(s):
		k = ''.join(format(ord(x), '02x') for x in s)
		return k

	# read .ass or .ssa file and produce revised new file
	def revision(self):
		self.set_ori_startline()
		self.set_tar_startline()
		if self.file_type == '.ass':
			self.create_newfile()
		else:
			self.create_newfile_ssa()
		for line in self.subfile:
			if re.match(r'^Dialogue: ', line) != None and \
				self.toms(self.ori_startline) <= \
				self.toms(re.search(ts_pattern, line).group()):
				self.outputfile.write(self.revise_event(line))
			else:
				self.outputfile.write(line)


if __name__ == '__main__':
	t = subtitle()
	t.revision()