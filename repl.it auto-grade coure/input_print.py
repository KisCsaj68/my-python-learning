#problems to solve with input/print
#sum of 3 numbers
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
#area of right triangle
b = int(input())
h = int(input())
a =1/2*b*h
print(a)
#prev and next
a = int(input())
print('The next number for the number ' +str(a)+ ' is ' +str(a+1))
print('The previous number for the number ' +str(a)+ ' is ' +str(a-1))
#hours and mins
N=int(input())
print(int(N/60//60), int(N//60))
#2 timestamp(diff to understand timestamp for this env.)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
print((d*3600+e*60+f)-(a*3600+b*60+c))
