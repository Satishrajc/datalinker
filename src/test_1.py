#!/usr/bin/python
# Import datalinker package
import datalinker

# Create an object using datalinker library
data = datalinker.DataLinker().run()

import test_2

if __name__ == '__main__':
	# Setting the data
	data.push("message", "Hello World!!")

	# Calling test_2.py without any arguments
	test_2.print_msg()