#string slicing(for single character)

j="welcomeworld"
print(j[0])
print(j[1])
print(j[2])
print(j[-2])
print(j[-3])
print(j[5])

#string slicing(substring)

m="whateverittakes"
print(m[0:10])
print(m[0:10:2])
print(m[:])
print(m[::-1])

#strings are immutable

k="fast"
k="p"+k[1:len(k)]
print(k)

#print() is used for displaying the output
#input("") is used for providing input from the user

a1="the"
b1="5"
c1="thiefs"
print(a1,b1,c1)#the comma is used for spacing purposes

p=int(input("Enter a number: "))#casting into int 
print(5*p)#input() takes string , casting is done

#example program

A=input("Enter a verb: ")
print("I can",A,"better than you")
print((A+" ")*5)

#Newton's method

cu=int(input("Enter the number to find the cube root of: "))
gu=int(input("Enter the initial guess:"))
newguess=gu-(gu**3-cu)/(3*gu**2)
print("Next guess to try=",newguess)

se=57
dd=int(input("Enter a number: "))
print(se == dd)

#branching using if , elif

num=int("75")
a=int(input("Enter a  number guess: "))
if a==num:
    print("the same as the secret number")
elif a>num:
    print("the guess is too high")
else:
    print("the guess is low")
    
