import time

kırmızı = '\033[91m'
mavi = '\033[94m'
varsayılan = '\033[0m'

X = kırmızı + "X" + varsayılan
O = mavi + "O" + varsayılan

# print(X) yazarsak kırmızı renkle X yazar.

oyun = []
for i in range(1, 10):
    oyun.append(str(i))

ad = input("Birinci oyuncunun adı (" + X + "): ")
birinci_oyuncunun_adı = kırmızı + ad + varsayılan

ad = input("İkinci oyuncunun adı (" + O + "): ")
ikinci_oyuncunun_adı = mavi + ad + varsayılan

for i in range(9):
    print("")
    print(oyun[0], oyun[1], oyun[2])
    print(oyun[3], oyun[4], oyun[5])
    print(oyun[6], oyun[7], oyun[8])
    print("")
    time.sleep(1)

    """
    Yani şöyle bir çıktı:
    1 2 3
    4 5 6
    7 8 9
    """

    if oyun[0] == oyun[1] == oyun[2] or \
        oyun[3] == oyun[4] == oyun[5] or \
        oyun[6] == oyun[7] == oyun[8] or \
        oyun[0] == oyun[3] == oyun[6] or \
        oyun[1] == oyun[4] == oyun[7] or \
        oyun[2] == oyun[5] == oyun[8] or \
        oyun[0] == oyun[4] == oyun[8] or \
        oyun[2] == oyun[4] == oyun[6]:

        if i % 2 == 0:
            print(ikinci_oyuncunun_adı, "KAZANDI!")
        else:
            print(birinci_oyuncunun_adı, "KAZANDI!")
        exit()

    if i % 2 == 0:
        tercih = int(input(birinci_oyuncunun_adı + ": "))
    else:
        tercih = int(input(ikinci_oyuncunun_adı + ": "))

    while True:
        if tercih < 1 or tercih > 9:
            tercih = int(input("1 ile 9 arasıda bir tamsayı girmelisiniz: "))
        # tercih'i indis olarak kullanmadan önce 1 çıkarmamız lazım.
        # Çünkü kullanıcı [1, 9] aralığında değer giriyor ama indisler [0, 8] aralığında.
        elif oyun[tercih - 1] in [X, O]:
        # veya şöyle de olur:
        #elif oyun[tercih - 1] not in "123456789":
            tercih = int(input("Boş olan bir kareyi seçmelisiniz: "))
        else:
            break

    if i % 2 == 0:
        oyun[tercih - 1] = X
    else:
        oyun[tercih - 1] = O


print("")
print(oyun[0], oyun[1], oyun[2])
print(oyun[3], oyun[4], oyun[5])
print(oyun[6], oyun[7], oyun[8])
print("")

print("BERABERE!")

"""
Egzersizler

Kolay:
Renkleri değiştirin. (Bkz. https://stackoverflow.com/a/287944/2772829)

Orta:
Oyuncular 3 oyun oynasın. En az 2'sini kazanan kazanmış sayılır.
(İlk 2 oyunu aynı kişi kazandıysa 3.'ye gerek kalmaz.)

Zor:
3x3 yerine 4x4'lük bir board olsun. Yine 3'lü zincir kuran kazanır.
Ama bu oyunu 3 kişi oynasın.
Buna benzer connect four adında bir oyun var. (Orada 2 kişi var ve 4'lü zincir kurmak gerekiyor.)
"""
