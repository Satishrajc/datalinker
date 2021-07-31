This package helps you to share the variables/data across the different Python files in the 
project/package. Once you set the variables in any Python file (.py) and if you want to access or fetch 
that in any other Python file in any location then you can do it easily with this package. You need to import the 
datalinker library in all the Python files to use this feature. We need import the package at the 
top of the file after that we can do push/pop the data. It is very simple to use this library just you need to install it, 
import it and use it.

## Supported data structure:
This library supports all the Python in-built data structures
1. String
2. Number
3. List
4. Tuple
5. Dictionary
6. Sets

## Advantages:
1. We need not to send arguments/parameters while calling the functions/method
2. Need not to return any variables/values from the function/method once you set the variables using push()
3. Easy to maintain the variables across the Python files
4. Need not to use global variables
5. Eliminates extra headache to maintain the variable and its names

## Installation
Run the following to install
```
pip install datalinker
```

## Usage
#### Import and create an instance
```
import datalinker
data = datalinker.DataLinker().run()
```

#### Setting the data
While pushing/setting the data give a unique name to the variable so that you can access it while pop()

```
data.push(variable_name, variable_value)
```

#### Getting the data
Whatever variable name you have provided in push() can be fetched as below

Example:

```
data.pop(variable_name)
```

## Example:
In the following example will set the variable "message" in the test_1.py and retrieve it test_2.py.

#### test_1.py

```
#!/usr/bin/python
# Importing data linker package
import datalinker

# Create a object using datalinker library
data = datalinker.DataLinker().run()

import test_2

if __name__ == '__main__':
	# Setting the data
	data.push("message", "Hello World!!")

	# Calling test_2.py without any argumnets
	test_2.print_msg()
```

#### test.py
```
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
```

#### NOTE:
1. Its case-sensitive hence be careful while pushing and popping the variables
2. Suppose if have not set the data abut if you try to access that using pop() method then will not return an error instead it will return None
3. Once the process is done then the variables will be destroyed