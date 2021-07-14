#Нгуен Ань Тхы
#ИУ7-16Б
from math import pow,sqrt
h=float(input('h='))
R=float(input('R='))
pi=3,14
a=sqrt(pow(R,2)-pow(R-h,2))
V=(pi*h/6)*(3*pow(a,2)+pow(h,2))
A=2*pi*R*h
print('{:30.5f}{:5.5f}',format('Обьем: ',V))
