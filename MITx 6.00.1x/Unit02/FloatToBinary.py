# Algo is to find a number big enough in the form of 2**p so that x*(2**p) is a whole number
# Convert the new whole number to binary
# divide this binary number by 2**p, which is actually shifting the new binary by p bits

x = float(input("Enter a floating point number to convert it to binary: "))

# step 1: find p such that x*(2**p) is a whole number i-e x*(2**p) % 1 == 0
p = 0
while (x*(2**p)) % 1 != 0:
    print("p: ", p, " x*(2**p): ", x*(2**p), " Remainder", x*(2**p) - int(x*(2**p)) )
    p +=1
print("p: ", p, " x*(2**p): ", x*(2**p), " Remainder", x*(2**p) - int(x*(2**p)) )

# step 2: convert the number to binary
result = ''
temp = int(x*(2**p))

while temp > 0:
    result = str(temp%2) + result
    temp = temp // 2

# step 3: 
# put leading zeros if result's len is less than p
for i in range(p - len(result)):
    result = '0' + result

# shift by p bits now i-e put a dot after p characters from left

result = result[0:-p] + "." + result[-p:]

print("float point representation of ", x, " is ", result)





