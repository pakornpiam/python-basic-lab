Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
friend = []
friend.append('AA')
friedn.append('BB')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    friedn.append('BB')
NameError: name 'friedn' is not defined. Did you mean: 'friend'?
friend.append('BB')
friend.append('CC')
print(friend)
['AA', 'BB', 'CC']
friend.append('DD')
print(friend)
['AA', 'BB', 'CC', 'DD']
friend.insert(0, 'EE')
print(friend)
['EE', 'AA', 'BB', 'CC', 'DD']
friend.insert(5, 'FF')
print(friend)
['EE', 'AA', 'BB', 'CC', 'DD', 'FF']
print(friend[-1])
FF
friend.insert(0, friend.pop(3))
print(friend)
['CC', 'EE', 'AA', 'BB', 'DD', 'FF']
friend.remove('AA')
print(friend)
['CC', 'EE', 'BB', 'DD', 'FF']
print(friend.remove('BB'))
None

print(friend)
['CC', 'EE', 'DD', 'FF']
print(friend.pop(1))
EE



print(friend)
['CC', 'DD', 'FF']





teacher = ('Q', 'S', 'Z')
teacher.append('Y')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    teacher.append('Y')
AttributeError: 'tuple' object has no attribute 'append'
AttributeError: 'tuple' object has no attribute 'append'
SyntaxError: invalid syntax
type(friend)
<class 'list'>
type(teacher)
<class 'tuple'>


coin = (5,10,10,10,5,1,1,1,2,2,5)
coin.count(10)
3
coin.count(1)
3



teacher = ('Q', 'S', 'Z')
teacher.index('S')
1
>>> print(teacher[-1])
Z
>>> ##### -1นับจากด้านหลัง -1 -2 -3... , นับจากด้านหน้า 0 1 2...###
>>> 
>>> character = ('A', 'D', 'E', 'T', 'Z', 'Y')
>>> character.sort()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    character.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> character = ['A', 'D', 'E', 'T', 'Z', 'Y']
>>> character.sort()
>>> 
>>> print(character)
['A', 'D', 'E', 'T', 'Y', 'Z']
>>> 
>>> 
>>> 
>>> character.sort(reverse=True)
>>> print(character)
['Z', 'Y', 'T', 'E', 'D', 'A']
>>> 
>>> sorted(character)
['A', 'D', 'E', 'T', 'Y', 'Z']
>>> 
>>> print(character)
['Z', 'Y', 'T', 'E', 'D', 'A']
>>> ['Z', 'Y', 'T', 'E', 'D', 'A']
['Z', 'Y', 'T', 'E', 'D', 'A']
>>> 
>>> 
>>> character.reverse()
>>> print(character)
['A', 'D', 'E', 'T', 'Y', 'Z']
>>> 
