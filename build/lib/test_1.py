#!/usr/bin/python
# Importing data linker package
import datalinker

# Create a object using datalinker library
data = datalinker.DataLinker().run()

import test_2

if __name__ == '__main__':
	# Setting the data
	data.push("message", "Hello World!!")

	# Calling test_2.py
	test_2.print_msg()