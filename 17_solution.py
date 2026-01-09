num = int(input("Enter the number:"))
temp = num
rev = 0
while num>0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if(rev == temp):
    print("is a palindrome")
else:
    print("is not a palindrome")