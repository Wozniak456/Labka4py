print("Возняк Софiя, 7 варiант")
print("")
n = int(input("Input n: "))
x1 = 1
x2 = 0.3
i = 3
if n < 1:
    print("ERROR input n > 0")
elif n == 1:
    print("x 1 =","%5.1f" % (x1))
elif n >= 2:
    print("x 1 =","%5.1f" % (x1))
    print("x 2 =","%5.1f" % (x2))

for i in range(3,n+1,1):
    xi = (i + 1)*x1 
    print("x",i,"=","%5.1f" % (xi))  

    x1 = x2
    x2 = xi

