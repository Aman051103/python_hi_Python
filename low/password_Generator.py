import random
a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c="0123456789"
s="!@#$%^&()"
x=a+b+c+s
y=16
password="".join(random.sample(x,y))
print(password)
