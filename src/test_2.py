#!/usr/bin/python

# Importing required modules
import datalinker
data = datalinker.DataLinker().run()

def print_msg():
    # Getting back the data
    name = data.get("message")
    print(f"The message is: {name}")