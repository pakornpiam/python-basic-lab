Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
friend = []
friend.append('AA')
friedn.append('BB')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    friedn.append('BB')
NameError: name 'friedn' is not defined. Did you mean: 'friend'?
>>> friend.append('BB')
>>> friend.append('CC')
>>> print(friend)
['AA', 'BB', 'CC']
>>> friend.append('DD')
>>> print(friend)
['AA', 'BB', 'CC', 'DD']
>>> friend.insert(0, 'EE')
>>> print(friend)
['EE', 'AA', 'BB', 'CC', 'DD']
>>> friend.insert(5, 'FF')
>>> print(friend)
['EE', 'AA', 'BB', 'CC', 'DD', 'FF']
>>> print(friend[-1])
FF
>>> friend.insert(0, friend.pop(3))
>>> print(friend)
['CC', 'EE', 'AA', 'BB', 'DD', 'FF']
>>> friend.remove('AA')
>>> print(friend)
['CC', 'EE', 'BB', 'DD', 'FF']
>>> print(friend.remove('BB'))
None
>>> 
>>> print(friend)
['CC', 'EE', 'DD', 'FF']
>>> print(friend.pop(1))
EE
>>> 
>>> 
>>> 
>>> print(friend)
['CC', 'DD', 'FF']
