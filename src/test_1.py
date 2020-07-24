import datalinker
data = datalinker.DataLinker().run()
import test2

# Setting the data
data.set("Name", "Satish")

# Calling test_2.py
test2.print_name()