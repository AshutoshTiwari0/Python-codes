"""
import ownmodule

# since now we have imported our own custom module we will call the function inside that
ownmodule.ownmod()
"""

# as keyword is used to declare a variable refering to the module acc to our choice
"""
import ownmodule as om
om.ownmod()
"""
"""
# another way of doing same thing
from ownmodule import ownmod
ownmod()
"""
"""
from ownmodule import ownmod as printing
printing()
"""

# we can also import each and every module like this. but it is not preferred.
"""
from random import *
print(random.randrange(3, 9))
"""
# this is preferred.
import random as r
print(r.randint(0,2))

