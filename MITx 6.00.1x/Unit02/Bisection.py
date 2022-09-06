from multiprocessing.connection import answer_challenge


x = 27
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (low + high)/2.0

while abs(ans**2 - x) >= epsilon:
    print("guess no: ", numGuesses)
    print("low:", low, " high", high, " ans ", ans);
    if ans**2 < x:
       low = ans
    else:
        high = ans
    ans = (low + high)/2.0

    numGuesses += 1

print("Guesses ", numGuesses)
print(ans, " is close enough to squre root of", x)



