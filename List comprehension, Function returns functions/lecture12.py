##List comprehension:
##    *Entire list operation can be given in single line.
##    *It consists of a function to apply, for loop to iterate through elements.
##    *And optional one , conditional statement is appended at the last , if user provides condition.
##    *Elements are taken through for loop , checks the condition , depending on the boolean values retrieved
##    from the condition, the function is applied.

##example:
def sqr_elem(L):
    List=[]
    for elem in L:
        List.append(elem**2)
    return List

L1=[1,2,3,4,5,6]
print(sqr_elem(L1))

##The above 4 lines of code inside function definition can be replaced in a single line using list comprehension

List=[elem**2 for elem in L1]
print(List)

List1=[elem**2 for elem in L1 if elem%2 != 0]##with conditions(if),(elem**2) is the function to be applied if cond is true
print(List1)

str=[len(x) for x in ["abc","abcd","adcde","7",7] if type(x)==str]
print(str)

##Default parameters inside function:
##    *If user provides the paremeter , then default value inside function has no effect .
##    *If the value for parameter is not provided , then the function uses the default value inside the function.

##Example bisection search

def bisection_root(x,epsilon=0.01):
    high=x
    low=0
    guess=(high+low)/2
    while abs(guess**2-x)>=epsilon:
        if guess**2 < x:
            low=guess
        else:
            high=guess
        guess=(high+low)/2
    return guess

print(bisection_root(123))##in this function call , epsilon value is 0.01 (i.e) default value(in function def) 
print(bisection_root(123,0.1))##(Here epsilon will be 0.1 specified in func call,default value will have no effect(0.01) )

##Aliasing of  function:
##Example

def is_even(x):
    return x%2==0

my_func=is_even#aliasing , both my_func & is_even gets binded to the same function object inside memory
print(my_func(10))
print(is_even(5))

##Function returns another function:

def func(a):
    def s(b):
        return a*b
    return s

##One way

var=func(5)(10)
print(var)

##other way

te=func(5)
var1=te(10)##chaining functions
print(var1)



