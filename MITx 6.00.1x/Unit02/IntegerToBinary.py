x = int(input("Enter the number you want to convert to binary: "))
isNeg = x < 0

ans = '';
temp = abs(x)

while temp > 0:
    remainder = temp % 2
    ans = str(remainder) + ans
     
    temp = temp//2


if isNeg:
    ans = "-" + ans;


print("Binary equivalent of ", x, " is ", ans)


