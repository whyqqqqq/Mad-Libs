print "Choose a month:",
month = raw_input()
print "Now choose a number:",
number = raw_input()
print "and now, a holiday:",
holiday = raw_input()
print "now, enter a noun in plural form:",
noun = raw_input()
print "now, a verb ending in 'ed':",
verbed = raw_input()
print "and a noun in plural form:",
noun2 = raw_input()
print "and a verb:",
verb2 = raw_input()
print "and another noun:",
noun3 = raw_input()
print "and yet another noun:",
noun4 = raw_input()
print "one more noun here:",
noun5 = raw_input()
print "and finally, enter an occupation:",
occupation = raw_input()

print """
	On %s %s every year, we celebrate %s.  
	All the %s get %s up in %s and %s all over the %s.  
	Many people love to eat their favorite %s or %s 
	much to their %s`s dismay.
	""" % (month, number, holiday, noun, verbed, noun2, verb2, noun3, noun4, noun5, occupation) 
