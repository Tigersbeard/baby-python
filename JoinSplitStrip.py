# join, split, strip

# help(str.join) help(str.split) help(str.strip)

# join(self, iterable, /)

#    Concatenate any number of strings.
#    The string whose method is called is inserted in between each given string.
#    The result is returned as a new string.
    
#    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
    
    
Line1="There once was a teacher called Sairam"
Line2="Who trained folks so AWS could hire'em"
Line3="The cloud was a mess"
Line4="They made a success"
Line5="And now nobody can fire'em"

Limerick='\n'.join([Line1 , Line2 , Line3 , Line4 , Line5])

# \n is the new line character in Python

#print(Limerick)


# split(self, /, sep=None, maxsplit=-1)

#   Return a list of the words in the string, using sep as the delimiter string.
    
#   sep
#     The delimiter according which to split the string.
#     None (the default value) means split according to any whitespace,
#     and discard empty strings from the result.
#   maxsplit
#     Maximum number of splits to do.
#     -1 (the default value) means no limit.


#print(Limerick.split("\n"))
#print("\n")
#print(Line3.split(" ", 2))


# strip(self, chars=None, /)
#   Return a copy of the string with leading and trailing whitespace removed.
    
#   If chars is given and not None, remove characters in chars instead.

print((Line3.strip("The c""mess")), "Laurens")

