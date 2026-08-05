from numpy import random

#generate random float numbers between 0 and 1
# x = random.rand(6)
# print(x)

#generate random numbers from array

# x = random.choice([3, 5, 7, 9],size=(3,4))
# print(x)


#probability distribution

x = random.choice([4,7,3,9],p=[0.1,0.3,0.6,0.0],size=(3,4))
print(x)