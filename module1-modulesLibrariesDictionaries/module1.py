#MODULES/LIBRARIES

#Another way to import a module:
from fibo import *
fib(100)

print ("Another way:")
print()

import fibo

fibo.fib(300)

print()

print("Random Number:")
import random
x = random.randrange(1,100)
print(x)


