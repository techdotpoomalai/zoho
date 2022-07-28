'''
Write a program to Validate an IPv4 Address.
According to Wikipedia, IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots, e.g., 172.16.254.1 .
A valid IPv4 Address is of the form x1.x2.x3.x4 where 0 <= (x1, x2, x3, x4) <= 255.
Thus, we can write the generalized form of an IPv4 address as (0-255).(0-255).(0-255).(0-255).
Note: Here we are considering numbers only from 0 to 255 and any additional leading zeroes will be considered invalid.

Your task is to complete the function isValid which returns 1 if the given IPv4 address is valid else returns 0. The function takes the IPv4 address as the only argument in the form of string.
'''

''' 
Example 1:

Input:
IPv4 address = 222.111.111.111
Output: 1
Explanation: Here, the IPv4 address is as
per the criteria mentioned and also all
four decimal numbers lies in the mentioned
range.

Example 2:

Input:
IPv4 address = 5555..555
Output: 0
Explanation: 5555..555 is not a valid
IPv4 address, as the middle two portions
are missing.
'''

def isValid(s):
    result=0
    split=s.split('.')
    for val in split:
        if len(val)>0 and len(val)<5:
            cheak=int(val)
            if cheak>=0  and cheak<=255 :
                result=1
            else:
                pass
    print(result)
ip='55.555'
isValid(ip)
