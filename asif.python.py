Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def full_pyramid(n):
...     for i in range(1, n + 1):
...         for j in range(n - i):
...             print(" ", end="")
...         
...         for k in range(1, 2*i):
...             print("*", end="")
...         print()
...    
