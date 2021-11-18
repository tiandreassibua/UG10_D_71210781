hm = int(input("Harga makanan sebesar Rp "))
hs = int(input("Harga snack sebesar Rp "))
hmin = int(input("Harga minuman sebesar Rp "))
uang = int(input("Uang yang anda bawa sebesar Rp "))

totalbelanja = hm+hs+hmin
print("Total yang harus anda bayar sebesar Rp",totalbelanja)
if totalbelanja > uang:
    print("Uang anda kurang! Anda memiliki utang sebesar Rp",(totalbelanja-uang))
elif totalbelanja == uang:
    print("Uang anda pas! Tidak ada Kembalian dan Utang :D")
else:
    print("Anda memiliki kembalian sebesar Rp",(uang-totalbelanja))