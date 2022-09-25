a = int(input("Enter the coefficient of x:"))
b = int(input("Enter the coefficient of y:"))
c = int(input("Enter the constant:"))
d = b**2 - 4*a*c
if d>0:
    print("Roots are real and distinct.")
elif d== 0:
    print("Roots are real and equal.")
else:
    print("Roots are imaginary.")
