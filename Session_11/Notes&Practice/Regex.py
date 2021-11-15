
#Regular Expression
'''
A Regular Expression (RegEx) is a sequence of characters that defines a search pattern
Python has a module named re to work with RegEx.
'''

#re.match()
'''
function to search pattern within the test_string. 
The method returns a match object if the search is successful
'''
import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

#MetaCharacters
'''
Metacharacters are characters that are interpreted in a special way by a RegEx engine. 
List of metacharacters:

[] . ^ $ * + ? {} () \ |

'''

#[] - Square brackets

'''
Square brackets specifies a set of characters you wish to match.
Eg:
[abc] will match if the string you are trying to match contains any of the a, b or c

You can also specify a range of characters using - inside square brackets.

    [a-e] is the same as [abcde].
    [1-4] is the same as [1234].
    [0-39] is the same as [01239].
    
Complement (invert) the character set by using caret ^ symbol at the start of a square-bracket.

    [^abc] means any character except a or b or c.
    [^0-9] means any non-digit character.


'''


#. - Period

'''
A period matches any single character (except newline '\n').
'''

#^ - Caret
'''
The caret symbol ^ is used to check if a string starts with a certain character.
Expression                  String                  Matched?
		
^a                              a                       1 match
		
                                abc                     1 match
		
                                bac                      No match
		


^ab                              abc                    1 match
		
                                acb                     No match (starts with a but not followed by b)

'''

pattern2 = '^ab '
test_string2 = str(input("\nEnter your input\n"))
result3 = re.match(pattern2, test_string2)
if result3:
  print("Match.")
else:
  print("No.")


pattern3 = '^a '
test_string3 = str(input("Enter your input\n"))
result2 = re.match(pattern3, test_string3)
if result2:
  print("Match ")
else:
  print("No Match")


#$ - Dollar
'''
The dollar symbol $ is used to check if a string ends with a certain character.

Expression              String                          Matched?
		
a$                          a                           1 match
		
                            formula                         1 match
		
                                    cab                     No match
		
'''

#* - Star
'''
The star symbol * matches zero or more occurrences of the pattern left to it.

Expression                      String                            Matched?
		
ma*n
				                mn                                  1 match
		
                                man                                 1 match
		
                                    maaan                                  1 match
		
                                    main                        No match (a is not followed by n)
		
                                woman                                       1 match
'''

pattern = 'ma*n'
test_string = input("Enter your input\n")
result = re.match(pattern, test_string)

if result:
  print("Match.")
else:
  print("No.")


#+ - Plus
'''
The plus symbol + matches one or more occurrences of the pattern left to it.
'''

pattern = 'ma+n'
test_string = input("Enter your input\n")
result = re.match(pattern, test_string)

if result:
  print("Match.")
else:
  print("No Match")

#? - Question Mark
'''
The question mark symbol ? matches zero or one occurrence of the pattern left to it.
'''

pattern = 'ma?n'
test_string = input("Enter your input\n")
result = re.match(pattern, test_string)

if result:
  print("Match.")
else:
  print("No Match")

#{} - Braces

'''Consider this code: {n,m}. This means at least n, and at most m repetitions of the pattern left to it.'''
pattern = 'a{2,3}'
test_string = input("Enter your input\n")
result = re.match(pattern, test_string)

if result:
  print("Match.")
else:
  print("No Match")

pattern = '[0-9]{2,4}'
test_string = input("Enter your input\n")
result = re.match(pattern, test_string)

if result:
  print("Match.")
else:
  print("No Match")


#| - Alternation

'''Vertical bar | is used for alternation (or operator).'''
pattern = 'a|b'
test_string = input("Enter your input\n")
result = re.match(pattern, test_string)

if result:
  print("Match.")
else:
  print("No Match")

#() - Group

'''Parentheses () is used to group sub-patterns. For example, (a|b|c)xz match any string that matches either a or b or c followed by xz'''
pattern = '(a|b|c)xz'
test_string = input("Enter your input\n")
result = re.match(pattern, test_string)

if result:
  print("Match.")
else:
  print("No Match")

#re.findall()
'''
The re.findall() method returns a list of strings containing all matches.
Example 1: re.findall()


# Program to extract numbers from a string
'''


string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string)
print(result)

# Output: ['12', '89', '34']
'''
If the pattern is not found, re.findall() returns an empty list.
re.split()

The re.split method splits the string where there is a match and returns a list of strings where the splits have occurred.
Example 2: re.split()
'''



string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string)
print(result)

# Output: ['Twelve:', ' Eighty nine:', '.']
'''
If the pattern is not found, re.split() returns a list containing the original string.

You can pass maxsplit argument to the re.split() method. It's the maximum number of splits that will occur.

'''


string = 'Twelve:12 Eighty nine:89 Nine:9.'
pattern = '\d+'

# maxsplit = 1
# split only at the first occurrence
result = re.split(pattern, string, 1)
print(result)

# Output: ['Twelve:', ' Eighty nine:89 Nine:9.']
'''
By the way, the default value of maxsplit is 0; meaning all possible splits.
re.sub()

The syntax of re.sub() is:

re.sub(pattern, replace, string)

The method returns a string where matched occurrences are replaced with the content of replace variable.
Example 3: re.sub()
'''

# Program to remove all whitespaces


# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.sub(pattern, replace, string)
print(new_string)

# Output: abc12de23f456
'''
If the pattern is not found, re.sub() returns the original string.

You can pass count as a fourth parameter to the re.sub() method. If omited, it results to 0. This will replace all occurrences.
'''


# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'
replace = ''

new_string = re.sub(r'\s+', replace, string, 1)
print(new_string)

# Output:
# abc12de 23
# f45 6

#re.subn()
'''
The re.subn() is similar to re.sub() except it returns a tuple of 2 items containing the new string and the number of substitutions made.
Example 4: re.subn()

'''
# Program to remove all whitespaces

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.subn(pattern, replace, string)
print(new_string)

# Output: ('abc12de23f456', 4)

#re.search()
'''
The re.search() method takes two arguments: a pattern and a string. The method looks for the first location where the RegEx pattern produces a match with the string.

If the search is successful, re.search() returns a match object; if not, it returns None.

match = re.search(pattern, str)

Example 5: re.search()
'''



string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")

# Output: pattern found inside the string
'''
Here, match contains a match object.
Match object

You can get methods and attributes of a match object using dir() function.

Some of the commonly used methods and attributes of match objects are:
match.group()

The group() method returns the part of the string where there is a match.
Example 6: Match object

'''


string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string) 

if match:
  print(match.group())
else:
  print("pattern not found")

# Output: 801 35
'''
Here, match variable contains a match object.

Our pattern (\d{3}) (\d{2}) has two subgroups (\d{3}) and (\d{2}). You can get the part of the string of these parenthesized subgroups. Here's how:
'''
match.group(1)


match.group(2)

match.group(1, 2)


match.groups()

'''
match.start(), match.end() and match.span()

The start() function returns the index of the start of the matched substring. Similarly, end() returns the end index of the matched substring.
'''
match.start()

match.end()
'''
The span() function returns a tuple containing start and end index of the matched part.
'''
match.span()

'''
match.re and match.string

The re attribute of a matched object returns a regular expression object. Similarly, string attribute returns the passed string.
'''
match.re
re.compile('(\\d{3}) (\\d{2})')





