##Bisection search algorithm:
##    1)It is the most efficient algorithm compared to guess-and-check and approximation algorithm
##    because it provides the solutions in a less number of iterations.
##    2)It needs a feedback to specify whether the guess is high or low , without feedback it
##    just like a guess and check.
##    3)It is applicable for statements which is defined orderly.
##    4)In the interval , we should provide the low and high endpoints.
##    5)In every iterations , low and high endpoints are changed accordingly
##    6)If answer greater than or less than the midpoint,change interval,repeat guessing by changing the
##    endpoints accordingly.
##    7)The guess is to be the midpoint of the interval(which is b/w low and high endpoint)


#finding square root of a number using bisection search(whole number)
sqr=81
epsilon=0.01
low=0
num_guesses=0
high=sqr
guess=(low+high)/2
while abs(guess**2-sqr)>=epsilon:
    if guess**2<sqr:
        low=guess
    else:
        high=guess
    guess=(low+high)/2
    num_guesses+=1
print(f"Number of guesses={num_guesses}")
print(f"{guess} is close enough to square root of {sqr}")

#finding square root of a number using bisection search(0 to 1)

sqr=0.5
epsilon=0.01
low=sqr
num_guesses=0   #low and high endpoints are changed
high=1
guess=(low+high)/2
while abs(guess**2-sqr)>=epsilon:
    if guess**2<sqr:
        low=guess
    else:
        high=guess
    guess=(low+high)/2
    num_guesses+=1
print(f"Number of guesses={num_guesses}")
print(f"{guess} is close enough to square root of {sqr}")

#combined form for finding square root (above  two cases in single program)

sqr=0.5
epsilon=0.01
if sqr<1:
    low=sqr
    high=1
else:
    low=1
    high=sqr
num_guesses=0
guess=(low+high)/2
while abs(guess**2-sqr)>=epsilon:
    if guess**2<sqr:
        low=guess
    else:
        high=guess
    guess=(low+high)/2
    num_guesses+=1
print(f"Number of guesses={num_guesses}")
print(f"{guess} is close enough to square root of {sqr}")

#finding cube root using (bisection search)
x=27
epsilon=0.01
low=0
num_guesses=0
high=x
guess=(high+low)/2
while abs((guess**3)-x)>=epsilon:
    if guess**3<x:
        low=guess
    else:
        high=guess
    guess=(high+low)/2
    num_guesses+=1
print(f"num guesses={num_guesses}")
print(f"{guess} is close enough to cube root of {x}")

#Newton rapshon method :
#    Applicable only for finding square root

x=49
guess=x/2
num_guesses=0
epsilon=0.01
while abs(guess*guess-x)>=epsilon:
    guess=guess-(((guess*guess)-x)/(2*guess))
    num_guesses+=1
print(f"num guesses={num_guesses}")
print(guess,"is close enough to cube root of",x)



