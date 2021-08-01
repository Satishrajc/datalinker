#!/usr/bin/python
# Import datalinker package
import datalinker

# Create an object using datalinker library
data = datalinker.DataLinker().run()


# Observe that no argument has Òbeen received in the function definition
def print_msg():
    # Getting back the data
    msg_data = data.pop("message")
    print(f"The message is: {msg_data}")
