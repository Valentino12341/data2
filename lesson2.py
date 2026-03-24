import numpy as np

array1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array1[0])
#SLICING OPERATOR 
print(array1[0:5])
print(array1[:7])
print(array1[6:10])
print(array1[6:])
print(array1[9:1:-1])

print(array1[::-1])# -1 means  reverses the array


newarray = np.array([1,2,3,4,5,6,7,8,9])
a=newarray.reshape(3,3)

print(a[0:2,0:2])


zevenroster = np.arange(1,50)
b=zevenroster.reshape(7,7)
print(b)
print(b[2:5,2:5])


oneto = np.array([1,2,3,4,5,6,7,8,9,10])

evenarr = oneto[oneto%2 ==0]
print(evenarr)

noteven = oneto[oneto%2 !=0]
print(noteven)

print(oneto[oneto==5])


print(oneto[oneto==15])


print(oneto[[1,4,7]])





newar = np.array([1,2,3,4,5,6,7,8,9,10])
print(newar[newar<=5])



listt = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(listt)):
    listt[i] +=10
    print(listt)




print(newar)
newar //= 2
print(newar)

a = np.array([7,8,9,25,17])
b = np.array([3,22,45,46,79])


result = a+b

print(result,"\n\n\n")


matA = np.random.permutation(np.arange(16)).reshape(4,4)
print(matA,"\n\n\n")

matB = np.random.permutation(np.arange(16)).reshape(4,4)
print(matB,"\n\n\n\n")

matresult = matA+matB
print(matresult)


def linear_equasion(x):
    y = (4*x)+8
    print(y)

linear_equasion(5)

x= np.array([2,4,6,8,10,12])
linear_equasion(x)


#task
print("\n\n\n\n\n\n\n\n\n\n\n")

taskar = np.arange(1,15)

anothertree = taskar[taskar<8]
anothertwo = taskar[taskar>=10]
anotherone = taskar[taskar%2 != 0]
print(anotherone)
print(anothertwo)
print(anothertree)
print(len(anotherone))
print(len(anothertwo))
print(len(anothertree))



#task2
print("\n\n\n\n\n\n\n\n\n\n\n")

twen = np.arange(1,20)
print(twen[0:5])
print(twen[14:])

print(twen[0:20:2])#start : end : step size 

print(twen[::-1])


























































































































































































































