#program to check if user entered number is odd or even using BITWISE operators
#returns true if n is even else Odd
def is_even_odd(n):
    #xor with 1 = n + 1 
    if (n ^ 1==n+1):
        return True
    else:
        return False
number = int(input("enter you number,,"))
if is_even_odd(number):
    print(number ,", is even")
else:
    print(number, "is odd")