s = 'azcbobobegghakl'

bob = 'bob'
count = 0;

for i in range(len(s)-1):
    if s[i:].find(bob) == 0:
        count += 1

print("Number of times bob occurs is: ", count)

