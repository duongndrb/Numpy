import numpy as np
#tao ma tran voi numpy
##  np.array(object, dtype=None, ndmin = 0)
#object - mang 2 chieu, co the la list cua list
#dtype - kieu du lieu cua cac phan tu trong ma tran
#ndmin - so chieu toi thieu khi return object

# khoi tao ma tran
_A = [[1,2,3],[4,5,6]]
A = np.array(_A)
#in ra ma tran
print(A)
#in ra gia tri hang 1 cot 2
print('a[0,1]:',A[0,1])
#in ra gia tri cac cot (cot2)
print('a[:,1]:',A[:,1])
#in ra gia tri cac hang(hang2)
print('a[1,:]:',A[1,:])

#khong the thao tac tren list

#khoi tao vecto
_B = [1,2,3,4,5,6]
B = np.array(_B)
print(B)