# pyco
when you need to create python script by python, this will help you 

### example 1 

STEP 1: make a TEST DIRECTORY and put the `pyco.py` there

STEP 2: make `hello_worlds_maker.py` with your editor

```
# hewllo_worlds_maker.py

import pyco
code = pyco.Pyco()
code.add('def hello_worlds():')
code.add('for i in range(5):')
code.add('print("Hello!")')
code.escape('b') # escape block
code.add('print("world!")')
code.escape('f') # escape function
code.add('if __name__ == "__main_":')
code.add('hello_worlds()')
code.make('hello_world.py')
```
STEP 3 : run your code

```
$ python hello_worlds.py
```
you will see `hello_world.py` in that directory

```
# hello_world.py

def hello_worlds():
    for i in range(5):
        print("Hello!")
    print("world!")    

if __name__ == "__main_":
    hello_worlds()
```

