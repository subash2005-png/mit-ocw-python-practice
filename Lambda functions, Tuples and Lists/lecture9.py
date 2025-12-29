##lambda functions:
##    *lambda functions are anonymous functions which does not have any name.
##    *It cannot be used whenever needed by calling a function like a ordinary function definition.
##    *It is used for a simple tasks,It is used only once.

print((lambda x:x%2==0)(8))#where lambda - keyword, x - parameter,(8)-input argument fed to x
print((lambda x:x%2==0)(5))

##example
def do_twice(n, fn):
    return fn(fn(n))
print(do_twice(3, lambda x: x**2))##evaluates to 81

##Tuples:
##    *Indexable ordered sequence of objects(int,string,tuple,tuple of tuples,...)
##    *Cannot change the values(objects) inside the tuple once created (immutable)..

tu=()##empty tuple
print(type(tu))
ts=(2,)##extra comma means tuple with one object , otherwise it just an integer not an tuple
t=(5,"hello",10)##multiple elements in tuples are separated by commas
print(t[0])##tuple slicing
c=(t+(10,100))
print(c)##concatenation of two tuples
print(c[1:2])
print(len(c))
print(c[1:3:2])#tuple slicing is similar to string slicing

##Iterating over objects in tuple
##Example:
s=(2,"a",4,(5,6),10)##here index 3 evaluates to subtuple (5,6) and index 4 evaluates to 10
for i in s:
    print(i)

##Swaping values using tuple:

x=10
y=100
(y,x)=(x,y)
print(x)
print(y)

##Tuples also used to return more than one value from a function

def quo_and_remain(x,y):
    c=x//y
    d=x%y
    return (c,d)

(quotient,remainder)=quo_and_remain(10,2)
print((quotient,remainder))


def count_char(s):
    """ s is a string of lowercase chars 
Return a tuple where the first element is the 
number of vowels in s and the second element 
is the number of consonants in s """
    b=0 ##simplest assignment (b,c)=(0,0)
    c=0
    for char in s:
        if char in "aeiou":
            b+=1
        else:
            c+=1
    return(b,c)

y="aeiouaeioushshshshsh"
(vowels,consonants)=count_char(y)
print(count_char(y))##returns the tuple
print("vowels=",vowels)#returns the count of vowels alone(int)
print("consonants=",consonants)

##to provide more arguments ,(i.e)user may provide inputs as their wish , tuples helps in such case

def mean(*argv):
    total=0
    for i in argv:
        total+=i
    mean=total/len(argv)
    return mean

print(mean(1,2,3,4,5))

##lists:
##    *Lists are also indexable ordered sequence of objects.
##    *It is represented inside square brackets [].
##    *It is mutable , which means values inside the list can be modified.
    
a=[]##empty list
l=[2,'ed',10,[5,6]]
c=l+[7,8]
print(c)

##sum of elements in a list
list1=[10,20,30,15,10,15]
total=0
for i in list1:##iterating over list
    total+=i
print(total)

##add the length of elements of a list

list2=["aaa","asd","qw","qe"]
total=0
for char in list2:
    len(char)
    total+=len(char)
print(total)

##defining function that has formal parameters as lists and return tuple
def sum_and_prod(L):
    """ L is a list of numbers 
Return a tuple where the first value is the 
sum of all elements in L and the second value 
is the product of all elements in L """
    (s,p)=(0,1)
    for i in L:
        s+=i
        p*=i
    return (s,p)

print(sum_and_prod([5,4,3,2,1]))










