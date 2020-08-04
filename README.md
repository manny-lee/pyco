# pyco
##When you need to create python script by python, this will help you.
* It makes indent for your python script automatically.
* you can get out of code-block, function, or class very simply.
* It makes blank lines between function or class automatically.


### example 1 

STEP 1: make a `TEST DIRECTORY` and put the `pyco.py` there

STEP 2: make `hello_worlds_maker.py` in that directory with your editor

```
# hello_worlds_maker.py

import pyco
code = pyco.Pyco()
code.add('# hello_worlds.py')
codd.addline()
code.add('def hello_worlds():')
code.add('for i in range(5):')
code.add('print("Hello!")')
code.escape('b') # escape block
code.add('print("world!")')
code.escape('f') # escape function
code.add('if __name__ == "__main__":')
code.add('hello_worlds()')
code.make('hello_worlds.py')
```
STEP 3 : run your code

```
$ python hello_worlds_maker.py
```
you will see `hello_worlds.py` in that directory

```
# hello_worlds.py

def hello_worlds():
    for i in range(5):
        print("Hello!")
    print("world!")    

if __name__ == "__main__":
    hello_worlds()
```

