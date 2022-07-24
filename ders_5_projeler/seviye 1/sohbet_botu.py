import random
import time
import datetime

if random.randrange(0, 100) < 5:   # %5'lik bir olasılık
    print("Tam ben çıkarken geldin.")
    time.sleep(1)
    print("Üzgünüm.")
    time.sleep(1)
    print("Ama bir gün görüşelim.")
    exit()

if random.randrange(0, 100) < 1:
    print("Bugün hiç konuşacak halim yok.")
    time.sleep(1)
    print("Başka bir gün görüşelim.")
    exit()

if random.randrange(0, 100) < 15:
    # Egzersiz: kullanıcı ne seçerse seçsin seçmediği bir şeyi tuttuğunuzu söyleyin.
    rastgele = random.randrange(1, 11)
    print("Aklımdan 1'den 10'a kadar bir tamsayı tuttum.")
    time.sleep(1)
    print("2 denemede bilirsen kazanırsın.")
    time.sleep(1)
    tahmin = input("Tahminin nedir?\n")
    if not tahmin.isdigit() or int(tahmin) < 1 or int(tahmin) > 10:
        print("Bir şey diyecektim de neyse.")
        time.sleep(1)
        print("Sana da yazık yani.")
        exit()
    if tahmin == rastgele:
        print("Vay canına, ilk denemede bildin!")
        time.sleep(1)
        print("Ama ben 2 denemede bilirsen kazanırsın demiştim.")
        exit()
    else:
        print("Yanlış...")
        time.sleep(1)
        print("Son hakkın.")
        ipucu = random.randrange(0, 100) < 25
        if ipucu:
            print("Hadi şanslı günündesin.")
            time.sleep(1)
            print("Bir ipucu vereyim.")
            time.sleep(1)
            if tahmin > rastgele:
                print("Daha küçük bir sayı denemelisin.")
            else:
                print("Daha büyük bir sayı denemelisin.")

        time.sleep(1)
        yeni_tahmin = input("Tahminin nedir?\n")

        if not yeni_tahmin.isdigit() or int(yeni_tahmin) < 1 or int(yeni_tahmin) > 10:
            print("Neyse anlaşamayacağız biz.")
            time.sleep(1)
            exit()
        yeni_tahmin = int(yeni_tahmin)
        if yeni_tahmin == tahmin:
            print("Sadece 2 hakkın vardı!")
            time.sleep(1)
            print("Niye aynı sayıyı söylüyorsun ki!?")
            exit()
        if ipucu and (yeni_tahmin < tahmin < rastgele or yeni_tahmin > tahmin > rastgele):
            print("Verdiğim ipucu boşa gitti.")
            time.sleep(1)
            print(rastgele, "tutmuştum.")
            exit()
        if yeni_tahmin == rastgele:
            print("Kazandın.")
            time.sleep(1)
            print("Şans işi tabii.")
            exit()
        print("Bilemeyeceğini biliyordum.")
        time.sleep(1)
        print(rastgele, "tutmuştum.")
        exit()


isimler = ["Ali", "Ayşe", "Mahmut", "Furkan", "Derya"]
benim_yaşım = 12

if random.randrange(0, 100) < 60:
    selamlama = "Merhaba!"
else:
    selamlama = "Selam!"

botun_ismi = isimler[random.randrange(0, len(isimler))]
# veya: botun_ismi = random.choice(isimler)

print(selamlama, "Benim adım", botun_ismi + ".")
time.sleep(1)
kullanıcının_ismi = input("Senin adın ne?\n")
time.sleep(1)

if len(kullanıcının_ismi) < 3:
    print("Herhalde dalga geçiyorsun!")
    time.sleep(1)
    print("Neyse başka zaman görüşürüz.")
    exit()

kullanıcının_ismi = kullanıcının_ismi[0].upper() + kullanıcının_ismi[1:].lower()
if kullanıcının_ismi == botun_ismi:
    print("İsmimiz aynı demek!")
else:
    print("Tanıştığımıza memnun oldum", kullanıcının_ismi + "!")
time.sleep(1)
print("Kaç yaşındasın", kullanıcının_ismi + "?")
time.sleep(1)
print("Dur, ben hesaplayayım...")
time.sleep(1)
doğum_yılı = int(input("Hangi yıl doğdun?\n"))

if doğum_yılı < 1900:
    print("Daha genç gösteriyorsun!")
    time.sleep(1)
    print("Neyse matematiğim o kadar iyi değil.")
    time.sleep(1)
    print("Benim şimdi gitmem lazım. Görüşürüz", kullanıcının_ismi + "!")
    exit()

şimdiki_yıl = datetime.datetime.now().year
if doğum_yılı > şimdiki_yıl:
    print("O halde daha doğmadın.")
    time.sleep(1)
    print("Sen doğduktan sonra görüşürüz.")
    exit()

yaş = şimdiki_yıl - doğum_yılı
print("O zaman yaklaşık", yaş, "yaşındasın.")
time.sleep(1)


if yaş == benim_yaşım:
    print("Benimle aynı yaştaymışsın.")
elif yaş < benim_yaşım:
    print("Yani benden biraz küçüksün.")
else:
    fark = yaş - benim_yaşım
    print("Yani benden", fark, "yaş büyüksün.")
    time.sleep(1)
    tahmin = int(input("O halde ben kaç yaşındayım?\n"))
    time.sleep(1)
    if tahmin == benim_yaşım:
        print("Evet bildin!")
    else:
        print("Matematiğin benimkinden bile kötüymüş.")

time.sleep(1)

renkler = ["beyaz", "siyah", "mavi", "kırmızı", "yeşil", "sarı", "pembe", "turuncu"]

yanlış_renk_örnekleri = ["penbe", "kirmizi"]
doğru_karşılıklar = ["pembe", "kırmızı"]

favori_renk = input("En sevdiğin renk hangisi?\n").lower()
time.sleep(1)
if favori_renk in renkler:
    print("Gerçekten mi!?")
    time.sleep(1)
    print("Benim de en sevdiğim renk", favori_renk + ".")
elif favori_renk in yanlış_renk_örnekleri:
    indis = yanlış_renk_örnekleri.index(favori_renk)        # Mesela penbe 0. eleman
    doğru_karşılık = doğru_karşılıklar[indis]               # Bu listedeki 0. eleman "penbe"nin doğru karşılığı.
    print("Onun doğru yazılışı", doğru_karşılık + ".")
else:
    print("Hmmm. Bu rengi daha önce hiç duymamıştım.")

time.sleep(1)
print("Taş-kağıt-makas oynamak ister misin?")
time.sleep(1)
print("Şimdiye kadar kimseye yenilmedim.")
cevap = input("").lower()

while True:
    if cevap in ["e", "evet", "olur", "tamam", "isterim"]:
        print("Neyse şimdi yenilmezliğimi bozmak istemiyorum.")
        break
    elif cevap in ["h", "hayır", "olmaz", "istemem", "yok"]:
        print("Korktun galiba.")
        time.sleep(1)
        print("Neyse önemli değil.")
        break
    elif cevap == "bilmiyorum":
        print("Bilmeyecek bir şey yok ki bunda.")
        time.sleep(1)
        print("Neyse hevesim kaçtı.")
    else:
        print("Evet ya da hayır demek bu kadar zor olmamalı.")
        cevap = input("Evet mi hayır mı?\n").lower()
        time.sleep(1)


time.sleep(1)
print("Benim çıkmam lazım. Yine görüşelim.")


"""
Egzersizler:

Çok kolay:
(1) Verileri arttırın:
Var olan listelere (isimler, renkler) yeni elemanlar ekleyin.
(2) Mesajları değiştirin:
Örneğin "İsmimiz aynı demek!" yazmak yerine "Benim de adım <...>" yazsın. 

Kolay:
(3) Sohbeti uzatın:
"Benim çıkmam lazım. Yine görüşelim." demeden önce bir şeyler daha konuşun.
(4) Daha akıllı veya gıcık bir bot:
yanlış_renk_örnekleri ve doğru_karşılıkları'na eklemeler yapın.
(5) Girilen renge özel mesajlar yazdırın:
Örneğin mor girilirse "Mor asaletin rengidir. Ben de severim" gibi şeyler yazsın.
Hatta bunu da olasılıksal yapın. Mesela mor girilirse %50 olasılıkla üstteki mesajı yazın, %50 olasılıkla da başka bir mesaj.

Orta:
(6) Yeni bir mod ekleyin.
Bu programda bir asıl program, 3 de bazen çalışan mod var (Modlar exit() ile bitiyor).
Belli bir olasılıkla çalışan yeni bir mod ekleyin.
İstediğiniz bir konuda sohbet edebilirsiniz veya hazır bir programın kodunu kopyalayabilirsiniz.
Örneğin hadi xox oynayalım diyip ilgili oyunun kodunu çalıştırabilirsiniz.
Veya mesela bilgi yarışmasına katılmak ister misin diye sorup kullanıcıyı bilgi yarışmasına sokabilirsiniz.

"""

