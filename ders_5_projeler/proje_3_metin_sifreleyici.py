# Sezar şifreleme algoritması

print("-" * 59)
print(" " * 10 + "METİN ŞİFRELEME VE ŞİFRE ÇÖZME PROGRAMI" + " " * 10)
print("-" * 59)

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz0123456789 ,."

while True:
    print("")
    print("Menüden bir seçim yapınız:")
    print("(1) Metni şifrele")
    print("(2) Şifreyi çöz")
    print("(3) Programı kapat")
    tercih = input("")
    while tercih not in ["1", "2", "3"]:
        tercih = input("Şunlardan birini seçebilirsiniz: 1, 2, 3\n")

    if tercih == "1":
        metin = input("Şifrelenecek metni giriniz: ").lower()
        anahtar = int(input("Şifreleme anahtarını giriniz (Pozitif tamsayı): "))

        şifre = ""
        for karakter in metin:
            if karakter in alfabe:
                şifre += alfabe[(alfabe.index(karakter) + anahtar) % len(alfabe)]
            else:
                şifre += karakter

        print("Şifreli metin:", şifre)

    elif tercih == "2":
        şifre = input("Çözülecek şifreyi giriniz: ").lower()
        anahtar = int(input("Şifreleme anahtarını giriniz (Pozitif tamsayı): "))

        metin = ""
        for karakter in şifre:
            if karakter in alfabe:
                metin += alfabe[(alfabe.index(karakter) - anahtar) % len(alfabe)]
            else:
                metin += karakter

        print("Şifresiz metin:", metin)

    else:
        break

    print("\n" + "-" * 59)

print("\n" * 2)
print("Güle güle. 👋")

"""
Egzersiz:
Şifreleme ve deşifreleme kodları birbirinin neredeyse aynısı.
Kod tekrarını azaltın. (Ortak olan kısımları birleştirin.)
Kod tekrarı azalırsa sonradan değişiklik yapmak kolaylaşır ve bazen kod da daha okunaklı olur.
Daha da önemlisi, kodda bir hata varsa bunu bulmak ve düzeltmek kolaylaşır.

Kod birleştirmeye bazı örnekler verelim.

...
if X:
    a()
    b()
    c()
    d()
    e()
    f()
    g()
else:
    a()
    h()
    i()
    c()
    d()
    e()
    j()
    g()
...
    
Yukarıdaki kodu şu şekilde değiştirebiliriz:

...
a()
if X:
    b()
else:
    h()
    i()
c()
d()
e()
if X:
    h()
else:
    j()
g()
...

Her iki kodda da X koşulu doğruysa a, b, c, d, e, h, g fonksiyonları; yanlışsa a, h, i, c, d, e, j, g fonksiyonları çağrılır.

Bazen satırlar birbirinin aynısı olmasa da belli bir formül altında birleştirilebilir:

...
if x % 2 == 0:
    y = 4
else:
    y = 5
...

x değişkeninin bir tamsayı olduğu biliniyorsa üstteki kod yerine alttaki yazılabilir:

...
y = 4 + x % 2
...

Çünkü x bir tamsayıysa x % 2 işleminin sonucu ya 0 olur ya da 1 olur. Bu durumda x çiftse y 4 olur, tekse 5 olur.

Değişkenlerin adları önemsizse elbette adları değiştirilerek birleştirilebilir:

...
if x > 0:
    mesaj = "x pozitiftir."
    print(mesaj)
else:
    ileti = "x pozitif değildir."
    print(ileti)
...

Üstteki yerine alttaki kod yazılabilir:

...
if x > 0:
    mesaj = "x pozitiftir."
else:
    mesaj = "x pozitif değildir."
print(mesaj)
...

Ortak kısımlar bütün satırlar değil, satırların belli kısımları olabilir:

...
if isim in kullanıcılar:
    fonksiyon1(fonksiyon2("Merhaba " + isim + "!").fonksiyon3())
else:
    fonksiyon1(fonksiyon2("Kullanıcı bulunamadı.").fonksiyon3())
...

Bu kod da altta şekilde yazılabilir:

...
if isim in kullanıcılar:
    mesaj = "Merhaba " + isim + "!"
else:
    mesaj = "Kullanıcı bulunamadı."
fonksiyon1(fonksiyon2(mesaj).fonksiyon3())
...

Satır adedi 4'ten 5'e çıkmış olsa da çok daha okunaklı bir kod elde edildi.
Hata varsa daha kolayca bulmak ve düzeltmek, hata yoksa bile sonradan kolayca değiştirebilmek için alttakini tercih etmek gerekir.

"""
