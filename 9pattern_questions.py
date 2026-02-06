n = int(input("enter number ")) 
def pattern(n):
    for i in range (1, n+1):
        print("*" * i)
pattern(n)

def pattern(n):
    for i in range (n, 0, -1):
        print("*" * i)
pattern(n)

def pattern(n):
    for i in range (1, n+1):
        for j in range (1, i+1):
            print(j, end=" ")
        print()
pattern(n)

def pattern(n):
    for i in range(1, n+1):
        print(str(i)*i)
pattern(n)



