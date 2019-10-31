# Strings
#   data that falls within " " marks

# Concatenation
# Put 2 or more strings together

firstName = "Fred"
lastName = "Flintstone"

fullName = firstName + " " + lastName

print(fullName)

# Repetition
#  Repetition operator: *

print("Hip " * 2 + "Hooray!")


def rowYourBoat():
    print("Row, " * 3 + 'your boat')
    print("Gently down the stream")
    print("Merrily, " * 4)
    print("Life is but a dream")


rowYourBoat()

# Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)
middleIndex = len(name) // 2
print(middleIndex)
print(name[middleIndex])

print(name[-1])

for i in range(len(name)):
    print(name[i])

# Slicing and Dicing
#   slicing operator: :
# slicing lets us make substrings

print(name[0:3])
print(name[:5])
print(name[6:9])
print(name[6:])

for i in range(1, len(name) + 1):
    print(name[0:i])

# Searching inside of Strings

print("biv" in name)
print("v" not in name)

if "y" in name:
    print("The letter y is in the name")
else:
    print("The letter y is not in the name")

    # String Methods to investigate:
    # Method        Use Example         Explanation
    # center        aStr.center(w)

string = "Frank N. Stein"

new_string = string.center(24)

print("Centered String: ", new_string)

# The string "center" moves the words or text over a certain amount of characters.

# ljust         aStr.ljust(w)

string = 'cat'
width = 5

print(string.ljust(width))

# the string ljust makes the total number of characters equal to the width.

# rjust         aStr.rjust(w)

string = 'dog'
width = 5
print(string.rjust(width))

# the string ljust makes the total number of characters equal to the width to the right.

# upper         aStr.upper()

string = "this should be uppercase!"
print(string.upper())
string = "Th!s Sh0uLd B3 uPp3rCas3!"
print(string.upper())

# the upper string makes any text in the string uppercase.
# lower         aStr.lower()

string = "THIS SHOULD BE LOWERCASE!"
print(string.lower())
string = "Th!s Sh0uLd B3 L0w3rCas3!"
print(string.lower())

# the lower string makes any text inside of the string lowercase
# index         aStr.index(item)

sentence = 'Python programming is fun.'
result = sentence.index('is fun')
print("Substring 'is fun':", result)
sentence = 'Java programming is fun'
result = sentence.index('Java')
print("Substring 'Java':", result)

# The index string uses the substring that is inside of the main string and prints that text.
# rindex        aStr.rindex(item)

quote = 'Let it be, let it be, let it be'

result = quote.rindex('let it')
print("Substring 'let it':", result)

quote = 'The world is so small'
result = quote.rindex('small')
print("Substring 'small ':", result)

# the rindex string is similar to index but if the substring is not found
# the result comes back as -1.

# find          aStr.find(item)

quote = 'Let it be, let it be, let it be'
result = quote.find('let it')
print("Substring 'let it':", result)
result = quote.find('small')
print("Substring 'small ':", result)

# If the substring exist the result is the index of the first occurrence if not -1.
# rfind         aStr.rfind(item)

quote = 'Let it be, let it be, let it be'
result = string.rfind('let it')
print("Substring 'let it':", result)
result = quote.rfind('small')
print("Substring 'small ':", result)

# If substring exists inside the string, it returns the highest index where substring is found.
# If substring doesn't exist inside the string, it returns -1.

# replace       aStr.replace(old, new)

song = 'cold, cold heart'
print(song.replace('cold', 'hurt'))
song = 'Let it be, let it be, let it be, let it be'
print(song.replace('let', "don't let", 2))

# Be sure to include multiple examples of all of them in use

# Character Functions

print(ord('B'))

print(chr(97 + 13))

print(str(12548))

# testing functions from mapper.py

from Mapper import *

print(letterToIndex('P'))
print(indexToLetter(10))

from Crypto import *

print(scramble2Encrypt("GOOD MORNING LADIES ADN GENTLEMEN"))
print(scramble2Encrypt("H ETN SA IEOLCTEMEIGI TFV COK"))
print(scramble2Decrypt(scramble2Decrypt(" T AIOCEEG F OHENS ELTMIITVCK")))

stripSpace("Who lives in a pineapple under the sea?")

print(caesarEncrypt("Alonzo is bullying me", 4))
