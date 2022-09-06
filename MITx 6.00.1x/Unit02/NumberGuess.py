print("Please think of a number between 0 and 100!")
low = 0
high = 100
ans = (low + high)//2

while True:    
    print("Is your secret number "+str(ans)+"?")
    print("Enter 'h' to indicate the guess is too high.", end=' ')
    print("Enter 'l' to indicate the guess is too low.", end= ' ') 
    print("Enter 'c' to indicate I guessed correctly.", end= ' ')
    choice = input()

    if choice == 'c':
        break
    elif choice == 'h':
        high = ans
    elif choice == 'l':
        low = ans
    else:
        print("Sorry, I did not understand your input.")

    if high == low:
        break
    
    ans = (high + low)//2

print("Game over. Your secret number was: ", ans);
