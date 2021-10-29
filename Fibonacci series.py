# Fibonacci-series
num=int(input("Enter a number : "))
x,y,z=(0,1,0)
while z<num:
    print(z)
    x=y
    y=z
    z=x+y
print("DONE!!")
