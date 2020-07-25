Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> string1 = "python programming"
>>> string1[0]
'p'
>>> string1[6]
' '
>>> string1[-1]
'g'
>>> string1[-2]
'n'
>>> #SLICING
>>> string1
'python programming'
>>> string1[0:5]
'pytho'
>>> string1[0:6]
'python'
>>> string1[7:18]
'programming'
>>> string1[3:]
'hon programming'
>>> string1[:10]
'python pro'
>>> string1[:]
'python programming'
>>> string1
'python programming'
>>> string1[0:18]
'python programming'
>>> string1[0:18:1]
'python programming'
>>> string1[0:18:2]
'pto rgamn'
>>> string1
'python programming'
>>> len(string1)
18
>>> string1[-1:-18:-1]
'gnimmargorp nohty'
>>> string1[-1:-19:-1]
'gnimmargorp nohtyp'
>>> string1[::-1]
'gnimmargorp nohtyp'
>>> #STRING FUNCTIONS
>>> string1
'python programming'
>>> string1.upper()
'PYTHON PROGRAMMING'
>>> string1 = "ABCDEF"
>>> string1.lower()
'abcdef'
>>> string1 ="Hello EveryOne, How are you?"
>>> string1.swapcase()
'hELLO eVERYoNE, hOW ARE YOU?'
>>> string1
'Hello EveryOne, How are you?'
>>> string1.capitalize()
'Hello everyone, how are you?'
>>> string1.title()
'Hello Everyone, How Are You?'
>>> name = "aahad"
>>> name.startswith('a')
True
>>> name.startswith('x')
False
>>> name.endswith('d')
True
>>> name.endswith('x')
False
>>> name
'aahad'
>>> name.count("a")
3
>>> name.count("h")
1
>>> name.count("x")
0
>>> string = "Sahil kumar"
>>> string.replace("kumar","Sharma")
'Sahil Sharma'
>>> string
'Sahil kumar'
>>> string = string.replace("kumar","Sharma")
>>> string
'Sahil Sharma'
>>> string.find('a')
1
>>> string.rfind('a')
11
>>> #find->first value
>>> #rfind->last value
>>> string.find(3,'a')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    string.find(3,'a')
TypeError: slice indices must be integers or None or have an __index__ method
>>> string
'Sahil Sharma'
>>> string.find('a',3)
8
>>> string.find('x')
-1
>>> string
'Sahil Sharma'
>>> string.index('a')
1
>>> string.index('a',2)
8
>>> string.index('x')
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    string.index('x')
ValueError: substring not found
>>> string
'Sahil Sharma'
>>> string.center(3)
'Sahil Sharma'
>>> string.center(5)
'Sahil Sharma'
>>> len(string)
12
>>> string.center(20)
'    Sahil Sharma    '
>>> string.center(20,'*')
'****Sahil Sharma****'
>>> string.center(15,"*")
'**Sahil Sharma*'
>>> string.center(15)
'  Sahil Sharma '
>>> string.center(19,"*")
'****Sahil Sharma***'
>>> string.center(19,"X")
'XXXXSahil SharmaXXX'
>>> string1 = "             aahad               "
>>> string1
'             aahad               '
>>> string1.lstrip()
'aahad               '
>>> string1
'             aahad               '
>>> string1.rstrip()
'             aahad'
>>> string1
'             aahad               '
>>> string1.strip()
'aahad'
>>> string2 = "################aahad###############"
>>> string2.lstrip("#")
'aahad###############'
>>> string2
'################aahad###############'
>>> string2.strip("#")
'aahad'
>>> string2 = "****aahad*****"
>>> string2.strip("*")
'aahad'
>>> string2
'****aahad*****'
>>> String1 = "Welcome to Our Python Programming Class"
>>> string1.split(" ")
['', '', '', '', '', '', '', '', '', '', '', '', '', 'aahad', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
>>> 
>>> String1
'Welcome to Our Python Programming Class'
>>> String1.split(" ")
['Welcome', 'to', 'Our', 'Python', 'Programming', 'Class']
>>> String1.split()
['Welcome', 'to', 'Our', 'Python', 'Programming', 'Class']
>>> string1 = "**Hello**ahaad**"
>>> string1.split("**")
['', 'Hello', 'ahaad', '']
>>> string ="ahaad"
>>> string.zfill(10)
'00000ahaad'
>>> string.zfill(22)
'00000000000000000ahaad'
>>> 