import time
import random

sorular = [
    ["Türkiye'nin başkenti neresidir?", ["Ankara", "İstanbul", "Londra", "Tahran"]],
    ["Bütün rakamların çarpımı kaç eder?", ["0", "45", "999", "2000"]],
    ["'Elma' kelimesinin İngilizce karşılığı nedir?", ["Apple", "Computer", "Pencil", "Cheese"]],
    ["Burj Khalifa'nin yüksekliği yaklaşık olarak kaç metredir?", ["800", "400", "1300", "2000"]]
]

# Bir soru şöyle bir yapıda:
# ["Soru metni", ["Doğru", "Yanlış", "Yanlış", "Yanlış"]]
# (Seçenekler karıştırılarak gösterilecek.)

soru_sayısı = 3

# Soru veri tabanından rastgele 3 tanesi rastgele bir sırada sorulur. Şıkların yerleri de rastgele olur.
random.shuffle(sorular)
sorular = sorular[:soru_sayısı]
ödül = 0

for soru in sorular:
    soru_metni = soru[0]
    seçenekler = soru[1]

    doğru_cevap = seçenekler[0]                     # Mesela "Ankara"
    random.shuffle(seçenekler)
    doğru_indis = seçenekler.index(doğru_cevap)     # Mesela 0
    doğru_seçenek = "ABCD"[doğru_indis]             # Mesela "A"

    print("-" * 50)

    print(soru_metni)
    print("(A)", seçenekler[0])
    print("(B)", seçenekler[1])
    print("(C)", seçenekler[2])
    print("(D)", seçenekler[3])
    seçim = input("Seçiminiz: ").upper()
    while seçim not in ["A", "B", "C", "D"]:
        seçim = input("Şıklardan birini seçiniz: ").upper()

    if seçim == doğru_seçenek:
        print("Doğru cevap!")
        ödül += 1000
        time.sleep(1)   # 1 saniye bekleyip sonraki soruyu gösterelim.
    else:
        print("Yanlış cevap!")
        break   # Yanlış cevap verilince bütün soruları görmeden eleniyoruz.


print("Para ödülü:", ödül, "TL")

"""
Egzersizler:

Çok kolay:
(Egzersiz 1) Sorulacak soru adedini 3'ten 4'e çıkarın. Bunun için tek bir değişkenin değerini değiştirmeniz lazım.

Kolay:
(Egzersiz 2) Soru havuzuna daha fazla soru ekleyin.

Orta:
(Egzersiz 3) Ödüller soru başına 1000 TL olmak yerine ilerledikçe 2'ye katlansın. (1000, 2000, 4000, 8000 şeklinde.)

Zor veya çok zor:
(Egzersiz 4) 
Yarışmacıya 1 defa kullanabileceği yarı yarıya joker hakkı verin.
Bu jokeri kullanınca yanlış olan seçeneklerden 2 tanesi kaybolur.
Menü tasarımı şöyle olabilir:

Türkiye'nin başkenti neresidir?
(A) İstanbul
(B) Ankara
(C) Tahran
(D) Londra
(1) Yarı yarıya joker hakkı
Seçiminiz: 1
Rastgele 2 yanlış şık elendi.
(B) Ankara
(C) Tahran
Seçiminiz: 

Yarışmacı joker hakkını kullandıysa (1) seçeneği gösterilmez.
(Ve 1 girse de "Geçersiz seçenek" veya "Jokerinizi zaten kullandınız" gibi bir uyarı gelir.

(Egzersiz 5)
Telefonda sorma joker hakkı da olsun.
Şöyle bir şey olabilir:
if %60 olasılıkla: doğru cevabı verecek
    if %40 olasılıkla:
        "Eminim ki cevap ..."
    else:
        "Sanırım cevap ..."
elif %50 olasılıkla (Ki elif olarak %50 normaldeki %20 olasılık oluyor): yanlış cevabı verecek
    if %20 olasılıkla:
        "Eminim ki cevap ..."
    else:
        "Sanırım cevap ..."
else: cevabı bilmeyecek
    if %50 olasılıkla:
        "Maalesef cevabı bilmiyorum."
    else:
        "Hiçbir fikrim yok."         


(Egzersiz 6)
Seyirciye sorma joker hakkı.
Seyirciler genelde haklı çıksın.
Toplamı 100 olacak şekilde bütün seçeneklere yüzdeler verilecek.

(Egzersiz 7)
Kendi programınızı yazabilirsiniz:
Şimdi buradan kopya çekerek (ama kopyala-yapıştır yapmadan) sıfırdan başka bir program yazın:
Quiz programı.
Bütün sorular kullanıcıya (öğrenciye) sorulsun. (Elenme diye bir kavram yok.)
Quiz bitince kaç doğru, kaç yanlış yapılmış, yüzde olarak başarı oranı vb. gösterilsin.
"""
