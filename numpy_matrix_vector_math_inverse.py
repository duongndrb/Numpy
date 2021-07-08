import numpy as np

#MA TRAN NGHICH DAO


_A = [[1,2,3],[4,5,6],[7,8,9]]
_B = [[1,2,3],[4,5,6]]
#khoi tao ma tran 
A = np.array(_A)
B = np.array(_B)
#ma tran nghich dao
A_i = np.linalg.pinv(A)

#in ma tran dao
print(A_i)
print(A_i@A)


##DAO MA TRAN '
print(A)
A__i = np.transpose(A)
#ma tran dao hang voi cot
print(A__i)

#LAY KICH THUOC CUA MATRAN
#so hang
print(np.size(B,0))
#so cot
print(np.size(B,1))

print(B)
#tong cac cot
print(np.sum(B,0))
#max min theo cot 
print(np.max(B,0))
print(np.min(B,0))

#tong cac hang
print(np.sum(B,1))
#max min theo hang 
print(np.max(B,1))
print(np.min(B,1))