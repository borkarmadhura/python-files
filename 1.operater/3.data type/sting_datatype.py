'''

String
======
1) sting is a collection of characters.
2)they are enclosed in single quote or double quote or triple quote
'''

#x='Itvedant'

#x= 4
'''
x=This ls a sting
multiline string
itvedant eclass learning
string
'''

x="Itvedant-Eclass"


print(x)
print(type(x))

#len(): This is used to calculate number of character in the string.

n=len(x)
print("total number of characters:",n)

#indexing
'''
To process string character by character, there is a need to access character in
the string. Indexing helps you to access character in the string.

There are two type of indexing:
1)positive indexing
2)negative indexing


positive index


      I  t  v  e  d  a  n  t - E  c  l  a  s  s
      0  1  2  3  4  5  6  7  8 9 10 11 12 13 14 


      
      I    t    v    e    d    a   n    t   -   E    c    l    a    s    s
     -15  -14  -13  -12  -11  -10  -9   -8 -7  -6   -5    -4   -3  -2   -1

syntax for accessing:
====================
 string_variable[index_number]


'''
'''
print(x[7])
print(x[12])
#print(x[16]) #Error=> index out of range
print(x[-11])
print(x[-5])
'''


#slicing

'''
need of slicing:
================
If there is need to extract partial part of the string from entire string,then use
slicing.

1) to reverse string.

syntax:

string_variable[start:stop:step]


      I  t  v  e  d  a  n  t - E  c  l  a  s  s
      0  1  2  3  4  5  6  7  8 9 10 11 12 13 14

Extract vedant word from the given string.

start=>2   stop=>8  step=>
'''

#x1=x[2:9:1]
#x1=x[10:15:1]


#x1=x[2:12:2]
#x1=x[2:8:] #default step in slicing is 1
#x1=x[:8:] # default star is 0
x1=x[::] #default stop = string end


#print(x1)

'''
slicing with negative index

                           Negative Index
      I    t    v    e    d    a   n    t   -   E    c    l    a    s    s
     -15  -14  -13  -12  -11  -10  -9   -8 -7  -6   -5    -4   -3  -2   -1


step==> negative

conclusion:
if step is positive then star=left   end=right
if step is negative then start=right end=left

'''

#x1=x[14:8:-1]  # 14,13,12,11,10,9
#x1=x[:8:-1]
x1=x[::-1]
print(x1)

















