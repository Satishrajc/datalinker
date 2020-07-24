This package helps you to share the data across the Python files. Once you set the data in any file and if you 
want to fetch it in any other Python file then you can do it easily with this package.
You need to import the *datalinker* library in all the Python files to use this feature. 
Once we import then we can do *get/set* the data.

## Installation
Run the following to install

```
pip install datalinker
```

## Usage
#### Import and create a instant
```
import datalinker
data_linker = datalinker.DataLinker().run()
```
#### Setting the data
While setting the data give a unique name to the variable so that you can access it while *get()*
```
data_linker.set("variable_name", "variable_value")
```

#### Getting the data
Whatever variable name you have provided in *set()* can be fetched as below
```
data_linker.get("variable_name")
```
#### Advantages:
1. We need not to send arguments/parameters while calling the functions
2. Need not to return any values from the function/modules once you set the variables using *get()*
3. Easy to maintain the variables across the Python files
5. Need not to use *global* variables 

## Example:
In the following example will set the *message* in the test_1.py and retrieve it test_2.py.

##### test_1.py
```
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
```
##### test_2.py
```
#!/usr/bin/python

# Importing required modules
import datalinker
data = datalinker.DataLinker().run()

def print_msg():
    # Getting back the data
    name = data.get("message")
    print(f"The message is: {name}")
```

##### Note: 
1. Its case sensitive hence carefully while setting and getting the variables
2. Suppose if have not set the data but if are trying to access that using *get()* method then 
will not get an error instead it will return *None*
3. Once the process is done then the variable will be destroyed