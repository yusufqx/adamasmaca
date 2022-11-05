print("""*****BİLGİLENDİRME*****
hatalı girdiğiniz her kelimede bir hak kaybedersiniz.
yanlış tahmin yaptığınız her kelimede bir hak kaybedersiniz.
Bu kelimeler arasından tahmin yapınız.
*****"kuş","kedi","köpek","kaplumbağa","balık","kartal","kurbağa","ayı","arı","domuz","sinek","yarasa"*****""")
import time
kelimeler=["kuş","kedi","köpek","kaplumbağa","balık","kartal","kurbağa","ayı","arı","domuz","sinek","yarasa"]
for harf in kelimeler:
    cevap="kedi"
hak=5
while True:
    tahmin=input("tahmin yazınız..")
    if tahmin not in kelimeler:
        print("lütfen geçerli bir kelime giriniz..")
        hak==5
        print("  --------  ")
        time.sleep(0.5)
        print("     O      ")
        time.sleep(0.5)
        print("     |      ")
    elif tahmin!="kedi":
        time.sleep(0.5)
        print("  --------  ")
        time.sleep(0.5)
        print("     O      ")
        time.sleep(0.5)
        print("     |      ")
        print("yanlış tahmin")

    elif tahmin == cevap:
        print("tebrikler doğru tahmin..")

        print("tahmininiz : {}\n cevap : {}".format(cevap, cevap))
        break
    tahmin = input("tahmin yazınız..")
    if tahmin not in kelimeler:
        print("lütfen geçerli bir kelime giriniz..")
        hak == 5
        print("  --------  ")
        time.sleep(0.5)
        print("     O      ")
        time.sleep(0.5)
        print("     |      ")

    elif tahmin!="kedi":
        time.sleep(0.5)
        print("  --------  ")
        print("     O      ")
        time.sleep(0.5)
        print("     |      ")
        time.sleep(0.5)
        print("    / \     ")
        print("yanlış tahmin")
        hak==4
    elif tahmin == cevap:
        time.sleep(0.5)
        print("  --------  ")
        time.sleep(0.5)
        print("     O      ")
        time.sleep(0.5)
        print("     |      ")

        print("tebrikler doğru tahmin..")
        print("tahmininiz : {}\n cevap : {}".format(cevap, cevap))
        break
    tahmin = input("tahmin yazınız..")
    if tahmin not in kelimeler:
        print("lütfen geçerli bir kelime giriniz..")
        hak==5
        print("  --------  ")
        time.sleep(0.5)
        print("     O      ")
        time.sleep(0.5)
        print("     |      ")

    elif tahmin!="kedi":
        time.sleep(0.5)
        print("  --------  ")
        print("   \ O /    ")
        time.sleep(0.5)
        print("     |      ")
        time.sleep(0.5)
        print("    / \     ")
        print("yanlış tahmin")
        hak==3
    elif tahmin==cevap:
        time.sleep(0.5)
        print("  --------  ")
        print("     O      ")
        time.sleep(0.5)
        print("     |      ")
        time.sleep(0.5)
        print("    / \     ")

        print("tebrikler doğru tahmin..")
        print("tahmininiz : {}\n cevap : {}".format(cevap, cevap))
        break
    tahmin = input("tahmin yazınız..")
    if tahmin not in kelimeler:
        print("lütfen geçerli bir kelime giriniz..")
        hak==5
        print("  --------  ")
        time.sleep(0.5)
        print("     O      ")
        time.sleep(0.5)
        print("     |      ")
    elif tahmin!="kedi":
        time.sleep(0.5)
        print("  --------  ")
        print("   \ O /|   ")
        time.sleep(0.5)
        print("     |      ")
        time.sleep(0.5)
        print("    / \     ")
        print("yanlış tahmin")
        hak==2
    elif tahmin==cevap:
        time.sleep(0.5)
        print("  --------  ")
        print("   \ O /    ")
        time.sleep(0.5)
        print("     |      ")
        time.sleep(0.5)
        print("    / \     ")
        time.sleep(0.5)

        print("tebrikler doğru tahmin..")
        print("tahmininiz : {}\n cevap : {}".format(cevap, cevap))
        break
    tahmin = input("tahmin yazınız..")
    if tahmin not in kelimeler:
        print("lütfen geçerli bir kelime giriniz..")
        hak==5
        print("  --------  ")
        time.sleep(0.5)
        print("     O      ")
        time.sleep(0.5)
        print("     |      ")

    elif tahmin!="kedi":
        time.sleep(0.5)
        print("  --------  ")
        print("   \ O_|/   ")
        time.sleep(0.5)
        print("     |      ")
        time.sleep(0.5)
        print("    / \     ")
        time.sleep(0.5)
        print("yanlış tahmin DİKKAT SON HAKKINIZ")
        hak==1
    elif tahmin==cevap:
        print("  --------  ")
        print("   \ O /|   ")
        time.sleep(0.5)
        print("     |      ")
        time.sleep(0.5)
        print("    / \     ")
        time.sleep(0.5)
        print("tebrikler doğru tahmin..")
        print("tahmininiz : {}\n cevap : {}".format(cevap, cevap))
        break
    tahmin = input("tahmin yazınız..")
    if tahmin not in kelimeler:
        print("lütfen geçerli bir kelime giriniz..")
        hak==5
        print("  --------  ")
        time.sleep(0.5)
        print("     O      ")
        time.sleep(0.5)
        print("     |      ")
    elif tahmin!="kedi":
        print("yanlış tahmin oyun bitti öldünüz")

        print("     O_|    ")
        time.sleep(0.5)
        print("    /|\      ")
        time.sleep(0.5)
        print("    / \     ")
        time.sleep(0.2)
        break
    if tahmin not in kelimeler:
        print("lütfen geçerli bir kelime giriniz..")
        hak==5
        print("  --------  ")
        time.sleep(0.5)
        print("     O      ")
        time.sleep(0.5)
        print("     |      ")
    elif tahmin==cevap:

        print("tebrikler doğru tahmin..")
        print("tahmininiz : {}\n cevap : {}".format(cevap,cevap))
        break
    if hak==0:
        break

