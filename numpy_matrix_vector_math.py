import numpy as np

#tao list 2 matran
_A = [[1,2,3],[4,5,6]]
_B = [[2,3,5],[7,9,21]]
#khoi tao ma tran 
A = np.array(_A)
B = np.array(_B)

print('A + B: \n', A+B)
#ket qua la:
#A + B:
# [[ 3  5  8]
# [11 14 27]]


print('A - B: \n', A-B)
#ket qua la:
#A - B:
# [[ -1  -1  -2]
# [ -3  -4 -15]]
##LUU Y: cong tru 2 ma tran co cung kich thuoc

### NHAN CHIA MA TRAN VOI MOT SO
print('A * 2: \n', A*2)

print('A / 2: \n', A/2)

##NHAN MA TRAN VOI VECTO
## so hang ma tran = so cot vecto
_C = [7,9,21]
C = np.array(_C)

#NHAN MA TRAN VOI VECTO
print('A*C: \n',A.dot(C))
#A.dot(C) tuong duong A@B voi py3.5 tro len
print('A*C: \n',A@C)

_D = [[1,2],[4,5],[6,7]]
D = np.array(_D)
##NHAN MA TRAN VOI MA TRAN
print('A*D: \n',A.dot(D))
#A.dot(C) tuong duong A@B voi py3.5 tro len
print('A*D: \n',A@D)

#MATRAN DON VI 
I = np.eye(5)
print(I)

#NHAN TUNG VI TRI TRONG MA TRAN
_E = [[1,2,3],[4,5,6]]
_F = [[1,2,3],[4,5,6]]

E = np.array(_E)
F = np.array(_F)
#ket qua cua phep nhan tung vi tri cua cac so trong ma tran
print(E*F)

#so sanh cac so trong ma tran bang voi 1
print(I == 1)

#so sanh cac so trong ma tran khac 1
print(I != 1)