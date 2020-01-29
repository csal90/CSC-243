Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> chr('a')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    chr('a')
TypeError: an integer is required (got type str)
>>> ord('a')
97
>>> chr(97)
'a'
>>> # charSet(low, high) that returns all the chracters whos ASCII code are
>>> # between low(int) and high(int), including both of them.
>>> # charSet(97, 99)
>>> # 'a'
>>> # 'b'
>>> # 'c'
>>> 
>>> def charSet(low, high):
	if i in range(low):
		print(chr(i))
	elif r in range(high):
		print(chr(r))

		
>>> 
