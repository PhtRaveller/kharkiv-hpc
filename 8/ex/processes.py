#!/usr/bin/python

if __name__ == "__main__":
	import os
	import time
	import sys
	print "I'm a parent. My ID is %i" % os.getpid()
	# Let's fork a child process
	cid = os.fork()
	# cid contains PID of child process when in parent and 0 when in child
	if cid == 0:
		# OK, we're in child process. Let's exec PDF viewer here
		print "I'm a child. My ID is %i" % os .getpid()
		os.execlp('evince', 'evince')
	else:
		print "I'm going to sleep for 20s."
		time.sleep(20)
		sys.exit()
