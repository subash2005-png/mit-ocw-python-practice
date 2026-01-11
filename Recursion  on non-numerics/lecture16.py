"""
Created on Thu Jan  8 22:27:52 2026

@author: Subash Chandar T
"""
# 1)Fibonacci series using recursion:

def fibo(a):
    if a==0 or a==1:
        return a
    else:
        return fibo(a-1)+fibo(a-2)
    
print(fibo(6))

#Efficient one:

def fibo_efficient(a):
    d={1:1,2:1}
    if a in d:
        return d[a]
    else:
        b=fibo_efficient(a-1)+fibo_efficient(a-2)
        d[a]=b
        return d[a]
    
print(fibo_efficient(6))

# for fibo(34), there are more than 10 million recursion takes place .
# for fibo_efficient(34), there are only 65 recursion takes place .

# 2)Sum of elements in a list using recursion:

def sum_of_list(l):
    if len(l)==1:
        return l[0]
    else:
        return(sum_of_list(l[1:])+l[0])

l=[10,10,20,50,30]
print(sum_of_list(l))

#  3)Sum of the length of string elements in a list using recursion

def sum_of_list_str(a):
    if len(a)==1:
        return len(a[0])
    else:
        return (len(a[0])+sum_of_list_str(a[1:]))

l1=["hello","hii","sorry"]
print(sum_of_list_str(l1))

# 4)Finding an element in a list using recursion

def find_elem(l,e):
    if len(l)==1:
        return l[0]==e
    elif l[0]==e:
        return True
    else:
        return (find_elem(l[1:],e))
        
l2=[2,1,8,2]
print(find_elem(l2,1))

# 5)Flatenning list containing list of integers

def flat_list(l):
    if len(l)==1:
        return l[0]
    else:
        return l[0]+flat_list(l[1:])
    
l3=[[1,2],[3,4],[5,6],[7,8],[9,10]]
print(flat_list(l3))

# 6)

def inner_find(l,elem):
    if len(l)==1:
        for e in l[0]:
            return e==elem
    elif elem in l[0]:
        return True
    else:
        return (inner_find(l[1:],elem))

l4=l3[:]
print(l4)
print(inner_find(l4,3))


    
