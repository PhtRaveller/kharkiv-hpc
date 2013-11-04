#!/usr/bin/python

if __name__=="__main__":
	import os
	import sys
	print "I expect, that MYVAR was set by shell."
	if os.environ.get('MYVAR', None):
		print "Yes, it was: \"%s\". Let's modify it." % os.environ['MYVAR']
		os.environ['MYVAR'] = "I was changed by Python process"
		exit_code = 0
	else:
		print "Oops, it wasn't. Let create it."
		os.environ['MYVAR'] = "I was set by Python process"
		exit_code = 1
	print "Value of MYVAR is \"%s\"" % os.environ['MYVAR']
	print "Remember, your calling shell doesn't see these changes."
	sys.exit(exit_code)	
