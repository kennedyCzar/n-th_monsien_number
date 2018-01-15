import random
'''
find the n-th Monisen number.
A number M is a Monisen number if M=2**P-1
and both M and P are prime numbers.
For example, if P=5, M=2**P-1=31,
5 and 31 are both prime numbers,
so 31 is a Monisen number.
Put the 6-th Monisen number into a
single text file and submit online.

n = input("enter the nth prime ")
number=10
p=2

while p <int(n):
    if all(number % i != 0 for i in range(2, number)):
        
        p = p+1   
    number = number+1
    m=2**p-1

print("6TH prime number: ",number-1,"and the monisen number is: ", m)

d=[i+1 for i in range(10) if i%2==0]
print(d)

sumA=0
i=1
while True:
    sumA +=i
    i+=1
    if sumA>10:
        break
print('i={}, sum={}'.format(i,sumA))


i = 1

while(i % 3):
    print(i, end = ' ')
    if (i >= 10):
        break
    i += 1
'''
def foo(num,base):
  	if(num >= base):
            foo(num // base , base)
        print(num%base, end = ' ')
        
numA = int(input())
numB = int(input())
foo(numA, numB)
