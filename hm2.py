import numpy as np


newarray = np.array([1,2,3,4,5,6,7,8,9])
a=newarray.reshape(3,3)

print(a[0:2,0:2])


zevenroster = np.arange(1,50)
b=zevenroster.reshape(7,7)
print(b)
print(b[2:5,2:5])

var10 = np.arange(1,37)

tenroster = np.arange(1,101)
a = tenroster.reshape(10,10)
print(a)

middlehokje = a[2:7, 2:7]
print(middlehokje)

eerste_rij = a[0]
print(eerste_rij)

laatste_rij = a[:,-1]
print(laatste_rij)

# SECOND 


def linear_equasion(x):
    y = (4*x)+8
    print(y)

linear_equasion(5)


linear_equasion(int(input("what number ??")))

#
def quadratic_equasion(x):
    y = (x**2)+5
    print(y)

quadratic_equasion(int(input("what num for quadratic")))
