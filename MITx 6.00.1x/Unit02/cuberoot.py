cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.001
num_guesses = 0

while abs(guess**3 - cube) >= epsilon and abs(guess**3) < abs(cube):
    guess += increment
    num_guesses +=1

print("number of guesses,", num_guesses);

if abs(guess**3) - cube >= epsilon:
   print("failed to find a cube root of", cube)
else:
   print(guess, "is close to cube root of", cube)