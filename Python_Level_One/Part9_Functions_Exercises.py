#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.


print("---------PROBLEM 1 ---------")
def arrayCheck(nums):
    # CODE GOES HERE
  for i in range(len(nums)-2):
    if nums[i==1] and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False
print(arrayCheck([1,2,3,4,5,6]))
print(arrayCheck([1,3,4,5,6]))
#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

print("---------PROBLEM 2 ---------")
def stringBits(str):
  result=""
  for i in range(len(str)):
    if i%2==0:
      result += str[i] 
  return result
print(stringBits("holi"))
print(stringBits("HHOOLLII"))
#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
"""
 end_other('Hiabc', 'abc')  True
 end_other('AbC', 'HiaBc')  True
 end_other('abc', 'abXabc')  True
"""
print("---------PROBLEM 3 ---------")
def end_other(a, b):
  # CODE GOES HERE
    return (b.lower().endswith(a.lower()) or a.lower().endswith(b.lower()))

print( end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc')) #todo=> ERROR
print(end_other('abc', 'abXabc'))
#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

"""
  # doubleChar('The')  'TThhee'
  # doubleChar('AAbb')  'AAAAbbbb'  
  # doubleChar('Hi-There')  'HHii--TThheerree'
  """ 
print("---------PROBLEM 4 ---------")
def doubleChar(str):
  result="";
  for char in str:
    result+=char
    result+=char
  return result

print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There') )


  # CODE GOES HERE


#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#

"""
# no_teen_sum(1, 2, 3)  6
# no_teen_sum(2, 13, 1)  3
# no_teen_sum(2, 1, 14)  3
"""
print("---------PROBLEM 5 ---------")
def no_teen_sum(a, b, c):
  # CODE GOES HERE
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
def fix_teen(n):
  if n in [13,14,15,16,17,18,19]:
    return 0
  return n
  # CODE GOES HERE
print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))
#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
"""
# count_evens([2, 1, 2, 3, 4])  3
# count_evens([2, 2, 0])  3
# count_evens([1, 3, 5])  0
"""
print("---------PROBLEM 6 ---------")
def count_evens(nums):
  count=0
  for i in nums:
    if i%2 == 0:
      count+=1
  return count
print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))