This package helps you to share the variables/data across the different Python files in the project/package. Once you set the variables in any Python file (.py) and if you want to access or fetch it back in any other Python file in any location/folder then you can do it easily with this package. You just need to import the datalinker library in all the Python files to use this feature. It is very simple to use this library.

## Supported data structure:
This library supports all the Python in-built data structures
1. String
2. Number
3. List
4. Tuple
5. Dictionary
6. Sets

## Advantages:
1. We need not send arguments/parameters while calling the functions/method
2. Need not return any variables/values from the function/method once you set the variables using push()
3. Easy to maintain the variables across the Python files
4. Need not use variables as global
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
While pushing/setting the data you have to provide a unique variable name so that you can access it while fetching it back with the same variable name.
```
data.push(variable_name, variable_value)
```

#### Getting the data
Whatever variable name you have provided in push() can be fetched using pop() as below
```
data.pop(variable_name)
```

## Example:
The following example will set the variable "message" in the test_1.py and retrieve it test_2.py.

#### test_1.py
```
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
```

#### test_2.py
```
#!/usr/bin/python
# Import datalinker package
import datalinker

# Create an object using datalinker library
data = datalinker.DataLinker().run()

# Observe that no argument has been received in the function definition
def print_msg():
    # Getting back the data
    msg_data = data.pop("message")
    print(f"The message is: {msg_data}")
```
Now, change the path to current directory and run the test_1.py
```
python test_1.py
```
Output:
```
The message is: Hello World!!
```

#### NOTE:
1. Its case-sensitive hence be careful while pushing and popping the variables names
2. Suppose if have not set the data and if you try to access that using the pop() method then it will return "None"
3. Once the code execution completes then the variables will be destroyed