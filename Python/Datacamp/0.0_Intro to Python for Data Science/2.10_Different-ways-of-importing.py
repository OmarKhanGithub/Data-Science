# 2.10
Different ways of importing
There are several ways to import packages and modules into Python. Depending on the import call, you'll have to use different Python code.

Suppose you want to use the function inv(), which is in the linalg subpackage of the scipy package. You want to be able to use this function as follows:

my_inv([[1,2], [3,4]])
Which import statement will you need in order to run the above code without an error?

INSTRUCTIONS
50 XP
Possible Answers
import scipy
press 1
import scipy.linalg
press 2
from scipy.linalg import my_inv
press 3
from scipy.linalg import inv as my_inv
press 4!!!
