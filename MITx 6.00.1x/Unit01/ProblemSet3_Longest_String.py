s = 'abcbcd'

current = s[0]
final = s[0]

for char in s[1:]:
    if char >= current[-1]:
        current += char
        if len(final) < len(current):
            final = current
    else:
        current = char



print ("Longest substring in alphabetical order is:", final)
