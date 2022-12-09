Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
vocab = {'cat':'แมว', 'dog':'หมา'}
vocab =[0]

vocab[0]
0


================================ RESTART: Shell ================================
vocab = {'cat':'แมว', 'dog':'หมา'}
vacab[0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    vacab[0]
NameError: name 'vacab' is not defined. Did you mean: 'vocab'?
vacab['cat']
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    vacab['cat']
NameError: name 'vacab' is not defined. Did you mean: 'vocab'?
vocab['cat']
'แมว'

vocab = ['cat':'แมว', 'dog':'หมา', 'pig': ['หมู','สุกร']}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
vocab = {'cat':'แมว', 'dog':'หมา', 'pig': ['หมู','สุกร']}
print(vocab['pig']
print(vocab['pig'])
      
SyntaxError: '(' was never closed
print(vocab['pig'])
      
['หมู', 'สุกร']
print(cocab['pig][0])
            
SyntaxError: incomplete input
SyntaxError: incomplete input
            
SyntaxError: incomplete input

print(vocab['pig'][0])
            
หมู
print(vocab['cat'][0])
            
แ

print(vocab['pig'][0][0])
            
ห

vocab['orang'] ='ส้ม'
            

print(vocab)
            
{'cat': 'แมว', 'dog': 'หมา', 'pig': ['หมู', 'สุกร'], 'orang': 'ส้ม'}
vocab['dog'] = ['สุนัช', 'หมา']
            
print(vocab)
            
{'cat': 'แมว', 'dog': ['สุนัช', 'หมา'], 'pig': ['หมู', 'สุกร'], 'orang': 'ส้ม'}


for i in vocab:
            print(i)

            
cat
dog
pig
orang


for i in vocab.item:
            print i
            
SyntaxError: incomplete input
for i in vocab.item:
            print(i)

            
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    for i in vocab.item:
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?


for i in vocab.item():
            print(i)

            
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    for i in vocab.item():
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
for i in vocab.items():
            print(i)

...             
('cat', 'แมว')
('dog', ['สุนัช', 'หมา'])
('pig', ['หมู', 'สุกร'])
('orang', 'ส้ม')
>>> 
>>> 
>>> for i in vocab.keys():
...             print(i)
... 
...             
cat
dog
pig
orang
>>> 
>>> for i in vocab.values():
...             print(i)
... 
...             
แมว
['สุนัช', 'หมา']
['หมู', 'สุกร']
ส้ม
>>> 
>>> 
>>> 
>>> x = [0,1], [4,['A', 'B', 'C', 99, 'Hello']]
...             
>>> x = [0,1], [4,['A', 'B', 'C', 99, 'Hello']]]
...       
SyntaxError: unmatched ']'
>>> x = [[0,1], [4,['A', 'B', 'C', 99, 'Hello']]]
...       
>>> print(x[1][1][4])
...       
Hello
