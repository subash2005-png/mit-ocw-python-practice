##To copy a list:
##    *A list's elements(top level) can be copied and it can be assigned to
##    new variable name.
##    *syntax: copied_list=L[:]
##    *We are just making the duplicate version of the original list,so
##    mutating the original list does not affect the copied list and vice versa
##    since they are different objects assigned to different variable name.
##Example
o_L=[1,2,3,4,5,10]
copy_list=o_L[:]
print(copy_list)
print(o_L)
print(id(copy_list))#id() function shows that these objects have different memory location
print(id(o_L))

##example
def remove_all(L, e):
    """L is a list
       Mutates L to remove all elements in L that are equal to e
       Returns None
    """
    li=L[:]
    L.clear()
    for elem in li:
        if elem != e:
            L.append(elem)

L = [1,2,2,2]
remove_all(L, 2)
print(L)

##Remove Operations on List:
##    *To delete a specific elment through index - del(L[index])
##    *L.pop() function usually remove the last element if it does not have any
##    parameters to specify to remove.If any value given inside it , it removes
##    the element corresponding to that index(value given inside() ).
##    It also returns the value that is removed.
##    *L.remove(element)- If an element given inside this function,it removes that
##    element in the list.

L11=[11,22,33,444,555,66,"hello",33,66,88,999,101010]
del(L11[11])
print(L11)
del(L11[5])
print(L11)
a=L11.pop(5)
print(L11)
print(a)##returns the element eliminated due to pop()

##example(using while loop)

def remove_All(L,e):
    while e in L:
        L.remove(e)
liss=[1,2,5,2,3,2]
remove_All(liss,2)
print(liss)

##above example(using while loop)

def remove_elem(L,e):
    l=L[:]
    for elem in l:
        if elem==e:
            L.remove(elem)
liss1=[1,2,5,2,3,2]
remove_elem(liss1,2)
print(liss1)

##program to remove duplicate elements between two list.

def remove_dup_elem(l,l1):
    ll=l[:]
    for elem in ll:
        if elem in l1:
            l.remove(elem)

list1=[1,2,5,2,3,2,10]
list2=[2,3,7,5,2]
remove_dup_elem(list1,list2)
print(list1)

##Aliasing:
##    *Aliasing means making a new variable name for an existing object(same list object referenced by another name).
##    *So,for an object binded to a variable name , we can make alias for same object.
##    *Mutating gets reflected to all variables binded to the same object.
##    *Shallow copy:copying the top level not including the inner list elements.
##    *Deepcopy:copying the entire top level and inner level(elements gets binded) of an list.

##Example
import copy
ss=[[1,2],[3,3],[4,4]]
sc=copy.copy(ss)##shallow copy,mutating the ss list ,does not affect the sc list when the top level of both are not shared
ss.append([5,5])
print(ss)
print(sc)


s11=ss[:]
dc=copy.deepcopy(s11)#deepcopy copies the top level and inner level,thus mutating any element in the s11 does not affect the deepcopied list
print(dc)
s11[0][1]=10
print(s11)
print(dc)


    







      

