import string
import time
from random import *

a = string.ascii_letters
d = string.digits
p = string.punctuation

karakterler = a + p + d

while 1:

    sayi = int(input("Şifreniz Kaç Haneli Olsun?\n(6'dan Daha Büyük Bir Sayı Giriniz.)\n>> "))

    if sayi <= 6:
        print("Lütfen Daha Büyük Bir Sayı Giriniz.")
        time.sleep(3)
        break

    sifre =  "".join(choice(karakterler) for x in range(randint(7, sayi)))
    print(sifre)

    saklama = input("Şifreyi Saklamak İstiyor Musunuz? (e/h?)\n>> ")

    if saklama == "e":
        sor = input("Şifreyi Hatırlamanız İçin Bir Ad Vermek İster Misiniz? (e/h?)\n>> ")
        if sor == "e":
            ad = input("Vermek İstediğiniz Adı Giriniz\n>> ")
            f = open("sifreler.txt", "a")
            f.write(sifre + "    Kaydedilen ad = " + ad)
            print("Şifreniz "+ad+" Adı İle Kaydediliyor...")
            time.sleep(1)
            print("Şifreniz Başarıyla Kaydedildi")
            yeni = input("Yeni Şifre Oluşturmak İstiyor Musunuz? (e/h?)\n>> ")
            if yeni == "h":
                print("Programdan Çıkılıyor...")
                time.sleep(2)
                break
        else:
            print("Adsız Bir Şekilde Şifreniz Kaydediliyor...")
            f = open("sifreler.txt", "a")
            f.write(sifre)
            time.sleep(1)
            print("Şifreniz Başarıyla Kaydedildi")
            yeni = input("Yeni Şifre Oluşturmak İstiyor Musunuz? (e/h?)\n>> ")
            if yeni == "h":
                print("Programdan Çıkılıyor...")
                time.sleep(2)
                break
    else:
        yeni = input("Yeni Şifre Oluşturmak İstiyor Musunuz? (e/h?)\n>> ")
        if yeni == "h":
            print("Programdan Çıkılıyor...")
            time.sleep(2)
            break