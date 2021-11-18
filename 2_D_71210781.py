a = int(input("Nilai a : "))
b = int(input("Nilai b : "))
c = int(input("Nilai c : "))

# rumus D = b² - 4ac
d = (b*b)-(4*a*c)
#print(float(d**(0.5)))

print("Nilai D adalah",d,"\n")

if d < 0:
   print("Fungsi tersebut tidak memiliki akar riil")

elif d == 0:
    x1 = (-b + d**(0.5)) / (2*a)
    print ("Fungsi tersebut memiliki akar kembar yaitu ",float(x1))

else:
    x1 = (-b + d**(0.5)) / (2*a)
    x2 = (-b - d**(0.5)) / (2*a)
    print("Akar akar dari persamaan tersbut adalah ",float(x1)," dan ",float(x2))