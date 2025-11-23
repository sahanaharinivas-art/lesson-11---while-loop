num = int(input("enter a number:"))
count = 0
n = num

if n==0:
    count = 1
else:
    while n>0:
        n=n//10
        count += 1

print("total digits:", count)