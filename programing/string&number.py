# msg="d5a1b2c4"
# out = ""

# '''This logic works on  number 1 to 9'''

# for ind in range(0, len(msg), 2):
#     out += (msg[ind] * int(msg[ind+1]))
# print(out)


'''This logic works on  number 1 to 99 but last digit is doble digit number'''
from types import NoneType


msg="a10b20c4a11"
out = ""

for ind in range(0, len(msg)-2):
    if msg[ind].isalpha()==1 and msg[ind+1].isdigit()==1 and msg[ind+2].isalpha()==1:
        out += (msg[ind] * int(msg[ind+1]))
    if msg[ind].isalpha()==1 and msg[ind+1].isdigit()==1 and msg[ind+2].isdigit()==1:
        out += (msg[ind] * int(msg[ind+1]+msg[ind+2]))
print(out)
# print(msg[11]==NoneType)