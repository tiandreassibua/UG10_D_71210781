bil1 = int(input("Masukan bilangan 1: "))
bil2 = int(input("Masukan bilangan 2: "))
bil3 = int(input("Masukan bilangan 3: "))

if (bil1 > bil2) & (bil1 > bil3):
    if bil3 > bil2:
        print("Urutan bilangan dari yang terbesar adalah",bil1,bil3,bil2)
    else:
        print("Urutan bilangan dari yang terbesar adalah",bil1,bil2,bil3)
elif (bil3 > bil1) & (bil3 > bil2):
    if bil1 > bil2:
        print("Urutan bilangan dari yang terbesar adalah",bil3,bil1,bil2)
    else:
        print("Urutan bilangan dari yang terbesar adalah",bil3,bil2,bil1)
else:
    if bil3 > bil1:
        print("Urutan bilangan dari yang terbesar adalah",bil2,bil3,bil1)
    else:
        print("Urutan bilangan dari yang terbesar adalah",bil2,bil1,bil3)