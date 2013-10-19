#!/usr/bin/env python

import sys
import re

# array to store dict of commit data
commits = []

def parseCommit(commitLines):
	# dict to store commit data
	commit = {}
	# iterate lines and save
	for nextLine in commitLines:
		if nextLine == '' or nextLine == '\n':
			# ignore empty lines
			pass
		elif bool(re.match('commit', nextLine, re.IGNORECASE)):
			# commit xxxx
			if len(commit) != 0:		## new commit, so re-initialize
				commits.append(commit)
				commit = {}
			commit = {'hash' : re.match('commit (.*)', nextLine, re.IGNORECASE).group(1) }
		elif bool(re.match('merge:', nextLine, re.IGNORECASE)):
			# Merge: xxxx xxxx
			pass
		elif bool(re.match('author:', nextLine, re.IGNORECASE)):
			# Author: xxxx <xxxx@xxxx.com>
			m = re.compile('Author: (.*) <(.*)>').match(nextLine)
			commit['author'] = m.group(1)
			commit['email'] = m.group(2)
		elif bool(re.match('date:', nextLine, re.IGNORECASE)):
			# Date: xxx
			pass
		elif bool(re.match('    ', nextLine, re.IGNORECASE)):
			# (4 empty spaces)
			if commit.get('message') is None:
				commit['message'] = nextLine.strip()
		else:
			print ('ERROR: Unexpected Line: ' + nextLine)

if __name__ == '__main__':
	parseCommit(sys.stdin.readlines())

	# print commits
	print 'Author'.ljust(15) + '  ' + 'Email'.ljust(20) +'  ' + 'Hash'.ljust(8) + '  ' + 'Message'.ljust(20)
	print "================================================================================="
	for commit in commits:
		print commit['author'].ljust(15) + '  ' + commit['email'][:20].ljust(20) + '  ' +  commit['hash'][:7].ljust(8) + '  ' + commit['message']
