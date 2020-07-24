this package helps you to share the data across teh Python files.
Once you set the data in any files and you wnat to fetch it in any other 
Python file then you can do it easily with this package.


## Installation
Run the following to install

```
pip install datalinker
```

## Usage
#### Import
```
import datalinker
data_linker = datalinker.DataLinker().run()
```
#### Setting the data
```
data_linker.set("varible_name", "variable_value")
```

#### Getting the data
```
data_linker.get("varible_name")
```

We need to import the files in all the Python files.
Once we import then we do *get/set* the data.