epsilon = 0.01
y = 24.0
g = y/2.0
numGuesses = 0


while abs(g*g - y) >= epsilon:
    print(g)
    numGuesses +=1
    g = g - ((g**2)-y)/(2*g)

print("numGuesses", numGuesses)
print("Square root of "+str(y)+" is about "+str(g))