#2 digits
a = int(input())
print(a//10,'',a%10)
#swap digits
a = int(input())
print(a%10*10+a//10,sep='')
#last 2 digits
print(int(input())%100)
#tens digit
b=int(input())
print(b//10%10)
#sum of digits
a = int(input())
print(
  a//100+
  a%100//10+
  a%10%10)
#digit after decimal
s = float(input())
print(int(s*10%10))
#car route
import math
a = int(input())
b = int(input())
print(math.ceil(b/a))
#century
a = 1901
b = int(input())
print(20+((b-a)//100))
#total cost
a = int(input())
b = int(input())
c = int(input())
print(a*c+b*c//100, b*c%100)
#day of week
A = int(input())
print((A - 365 + 4)% 7)
#digital clock
N = int(input())
print(N//60,N%60)
#The hour hand of an analog clock turned α degrees since the midnight. Determine the angle by which the minute hand turned since the start of the current hour. Input and output in this problems are integers.
a = int(input())
print(a%30*2*6)
#school desks
a = int(input())
b = int(input())
c = int(input())
print(a//2+a%2+b//2+b%2+c//2+c%2)
