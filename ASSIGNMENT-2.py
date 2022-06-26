#create a string and access by using for loop
a=('SHRUTIKA')
for i in a:
	print(i)
print()

#Write an example for indexing (forward and backward)
a=('elearninfotech')
print(a[1])
print(a[5])
print(a[-3])
print(a[-7])
print()

#write an example for slicing:
a=('elearninfotech')
print(a[1:5])
print(a[4:9])
print(a[1:8:2])
print(a[-1:-6])
print()

#write an example program for arithmetic operators
def calc(a,b):
	sum=a+b
	sub=a-b
	mul=a*b
	div=a/b
	return sum,sub,mul,div
m=int(input('Enter First Number:'))
n=int(input('Enter Second Number:'))
result=calc(m,n)
print('Addition:',result[0])
print('Substraction:',result[1])
print('Multiplication:',result[2])
print('Division:',result[3])
print()
#write an example program for identity operators
a=[10,20,30]
b=[30,40,50]
c=[10,20,30]
print(a is b)
print(a is not b)
print(a is c)
print(b is not c)
print() 

#Find the largest number amongest 3 numbers
a=int(input('Enter First Number:'))
b=int(input('Enter Second Number:'))
c=int(input('Enter Third Number:'))
if a>b and a>c:
	print(a,'is largest number')
elif b>c:
	print(b,'is largest number')
else:
	print(c,'is largest number')
print()

#write an example program ( Find given number is even number or odd number)
def evenodd(n):
	if n%2==0:
		print(n,'is even number')
	else:
		print(n,'is odd number')
n=int(input('Enter Number:'))
evenodd(n)
print()

#write an example program for for loop
for x in range(21):
	if x%2==0:
		print(x)

