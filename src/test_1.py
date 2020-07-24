#!/usr/bin/python
# Importing required modules
import test_2
import datalinker
data = datalinker.DataLinker().run()

if __name__ == '__main__':
	# Setting the data
	data.set("message", "Hello World!!")

	# Calling test_2.py
	test_2.print_msg()