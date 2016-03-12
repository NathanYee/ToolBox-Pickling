""" A program that stores and updates a counter using a Python pickle file"""

import os
import sys
import pickle

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
                doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""
        if os.path.exists(file_name) == False or reset == True:
            fout = open(file_name, 'w') #open file in write only because will not need to read
            fout.write(pickle.dumps(1)) #convert 1 to pickle string
            fout.close
            return 1
        else:
            fout = open(file_name, 'r+') #open file in read+ mode so we can both read and write
            pickled = fout.read()
            unpickled = pickle.loads(pickled)
            new_counter = unpickled + 1
            fout.seek(0,0) #move pointer to the first line, first index.
                           #This will allow us to write over the counter.
                           #As of this point, I don't think we can go over 10 as we will not
                           #write over the second digit
            fout.write(pickle.dumps(new_counter)) #convert new_counter to pickle string
            fout.close

            return unpickled + 1


if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))
