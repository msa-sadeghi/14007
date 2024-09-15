names = ("roze", "sara", "artin", "nikan")
print(names[0:4:2])
print(names[::2])


names = ()
n1 = input("enter a name:> ")
names += (n1,)
n1 = input("enter a name:> ")
names += (n1,)
n1 = input("enter a name:> ")
names += (n1,)
print(names)
print(names[::2])
