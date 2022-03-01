# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:"))
# a,b=[int(x) for x in input().spit()]
# print(a,b)

# a=int(input("Enter the value of a:"))
# if(a==5):
#     print("yes Equal")

a,b=[int(x) for x in input().split()]
if(a>b):
    print(f"{a}>{b} is {a>b}")
else:
    print(f"{a}>{b} is {a>b}")