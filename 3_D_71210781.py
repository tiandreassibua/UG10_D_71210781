# foo = ["Iwo", "Abdur", "Vegas"]
# inp = input("Input : ")
# if inp in foo:
#     print(inp,"sudah ada dalam daftar")
# else:
#     foo.append(inp.upper())
#     print(inp, "berhasil ditambahkan kedalam daftar\n")
#     print(foo)

# daftar = []
# daftarnama = input("Masukan nama barang: ")

# daftar.append(daftarnama)

# print(daftar)

# shampoo clear, beras, kecap

# ['shampoo clear','beras','kecap']

inp = input("Masukan daftar belanja : ").title().split(",")
print("Daftar belanja :",inp)

addinp = input("Masukan barang yang ingin ditambahkan : ").lower()
if addinp.title() in inp:
    print(f"Barang {addinp.upper()} sudah berada dalam daftar belanja")
else:
    inp.append(addinp.upper())
    print(f"Hasil penambahan pada daftar belanja {inp}")