import random

#get the desired length for the password from the user
passlen = int(input('enter the length of the password: '))

#define the character set for the password
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTWXYZ0123456789!@#$&*"

#generate a random password by sampling characters from 's'
p = "".join(random.sample(s, passlen))

#print the generated password
print('generated password: ', p)