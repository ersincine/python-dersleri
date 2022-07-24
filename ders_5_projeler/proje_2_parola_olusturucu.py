import random

uzunluk = int(input("Parolada kaç karakter bulunsun? "))
while uzunluk <= 0:
    uzunluk = int(input("Lütfen pozitif bir tamsayı girin: "))

büyük_harf = input("Büyük harf bulunsun mu? (e/h) ").lower() in ["e", "evet"]
küçük_harf = input("Küçük harf bulunsun mu? (e/h) ").lower() in ["e", "evet"]
rakam = input("Rakam bulunsun mu? (e/h) ").lower() in ["e", "evet"]
özel_karakter = input("Özel karakter bulunsun mu? (e/h) ").lower() in ["e", "evet"]

bütün_karakterler = ""
if büyük_harf:
    bütün_karakterler += "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
if küçük_harf:
    bütün_karakterler += "abcçdefgğhıijklmnoöprsştuüvyz"
if rakam:
    bütün_karakterler += "0123456789"
if özel_karakter:
    bütün_karakterler += ".:,;!?+-"

parola = ""
for _ in range(0, uzunluk, 1):
    parola += random.choice(bütün_karakterler)
print("Parolanız:", parola)

"""
Egzersiz:
Eğer kullanıcı sorulara "e" veya "evet" yazarsa, hatta örneğin "EVET" (çünkü lower fonksiyonu ile harfler küçültülüyor zaten) yazarsa
sorulan özelliği kabul ettiği anlamına gelir, bütün aksi girdilerse reddettiği anlamına gelir.
Şimdi şunu yapın: Eğer kullanıcı cevabı boş bırakırsa da soruyu onayladığı varsayılsın.

Egzersiz:
Kullanıcıya Türkçe ve İngilizce seçeneklerini sunup harf seçiminde seçilen dilin alfabesi kullanılsın.
İngilizce seçilirse büyük harf seçeneklerinde örneğin Ğ olmayacak ama fazladan örneğin X olacak.

Egzersiz:
Kullanıcı parolanın uzunluğu için en_az_uzunluk ve en_fazla_uzunluk değerlerini girsin. 
Program [en_az_uzunluk, en_fazla_uzunluk] aralığında rastgele bir uzunlukta parola üretsin.
Mesela 8 ve 12 girilirse, uzunluk rastgele olarak belirlenip örneğin 10 olacak.

Egzersiz:
Kullanıcı büyük harf bulunsun dediğinde biz büyük harfleri seçeneklerimiz arasına koyuyoruz.
Ama yine de parolada büyük harf denk gelmeyebilir (özellikle de uzunluk azsa).
İstenenin olmasını garantileyecek şekilde kodu değiştirin.

Mesela şöyle olabilir:
Parola sonsuz bir döngü içinde oluşturulur. Eğer istenen şart sağlanmışsa döngüden çıkılır.
İstenen şartlar örneğin büyük harf için şöyle kontrol edilebilir:
if "A" in parola or "B" in parola or "C" in parola ...
Tabii kodu bu şekilde yazmak çok uzun olur. Onun yerine şöyle olabilir:
if len(set("ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ").intersection(parola)) >= 1:
Yani seçeneklerimizi bir kümeye (set) dönüştürüyoruz.
Böylece kesişim (intersection) metodunu kullanabiliyoruz.
Büyük harflerle parolanın kesişimi en az 1 elemanlıysa şartımız sağlanmıştır.) 
Bu 1 satırlık kodu okuması size zor gelebilir ama bunu bir kere anlarsanız sizin için çok faydalı olacak.

(Normal) fonksiyonlar şöyle kullanılır:

fonksiyon(argümanlar)
Örneğin print(1, 2, 3)
Bu tarz fonksiyonlardan bazıları modüllerin altında tanımlıdır:
modül.fonksiyon(argümanlar)
Örneğin random.randint(1, 6)

Metot denen fonksiyonlar ise şöyle kullanılır:
nesne.metot(argümanlar)

Nesneler hakkında daha fazla şeyi ilerleyen derslerde öğrenebilirsiniz.
Şimdilik şunu bilin: Nesnemiz değişken şeklinde de olabilir literal şeklinde de.
Örneğin:
x = "ABC" olsun.
x.lower() veya "ABC".lower() yazarak "abc" elde ederiz (Bütün harfler küçültülür).

str'lerin kendilerine ait metotları var (lower, replace vb.)
list'lerin kendilerine ait metotları var (append, sort vb.)
set'lerin kendilerine ait metotları var (intersection, union vb.)

set("123") gibi bir şey yazarak bir küme oluşturuyoruz.
Aslında int("123") şeklinde çağrılan int fonksiyonuna çok benziyor set fonksiyonu.
int nasıl ki bir tamsayı oluşturuyor, set de bir küme oluşturur.
Öyle ki kümenin elemanları "1", "2" ve "3" olur.
Sonra bunun üzerinden intersection metodunu kullanıyoruz.
Argüman olarak da neyle kesişimini hesaplayacağımızı yazıyoruz.
Sonuç yine bir küme oluyor. len fonksiyonu ile eleman adedine bakıyoruz.
"""
