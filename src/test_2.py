import datalinker
data = datalinker.DataLinker().run()

def print_name():
    # Getting back the data
    name = data.get("Name")
    print(f"The name is: {name}")