#!/usr/bin/python
# Importing data linker package
import datalinker

# Create a object using datalinker library
data = datalinker.DataLinker().run()

import test_2


def print_msg():
    # Getting back the data
    msg_data = data.pop("message")
    print(f"The message is: {msg_data}")