print("""*****BİLGİLENDİRME*****
eğer bu kelimeler arasından tahmin yapmaz iseniz 5 kelime sonrasında hakkınız bitecektir.
Bu kelimeler arasından tahmin yapınız.
*****"kuş","kedi","köpek","kaplumbağa","balık","kartal","kurbağa","ayı","arı","domuz","sinek","yarasa"*****""")
import time
kelimeler=["kuş","kedi","köpek","kaplumbağa","balık","kartal","kurbağa","ayı","arı","domuz","sinek","yarasa"]
for harf in kelimeler:
    cevap="kedi"

while True:
    tahmin=input("tahmin yazınız..")
    if tahmin not in kelimeler:
        print("lütfen geçerli bir kelime giriniz..")

    elif tahmin!="kedi":
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
    elif tahmin!="kedi":
        print("  --------  ")
        print("     O      ")
        time.sleep(0.5)
        print("     |      ")
        time.sleep(0.5)
        print("    / \     ")
        print("yanlış tahmin")
    elif tahmin == cevap:
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
    elif tahmin!="kedi":
        print("  --------  ")
        print("   \ O /    ")
        time.sleep(0.5)
        print("     |      ")
        time.sleep(0.5)
        print("    / \     ")
        print("yanlış tahmin")

    elif tahmin==cevap:
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
    elif tahmin!="kedi":
        print("  --------  ")
        print("   \ O /|   ")
        time.sleep(0.5)
        print("     |      ")
        time.sleep(0.5)
        print("    / \     ")
        print("yanlış tahmin")
    elif tahmin==cevap:
        print("  --------  ")
        print("   \ O /    ")
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
    elif tahmin!="kedi":
        print("  --------  ")
        print("   \ O_|/   ")
        time.sleep(0.5)
        print("     |      ")
        time.sleep(0.5)
        print("    / \     ")
        print("yanlış tahmin DİKKAT SON HAKKINIZ")
    elif tahmin==cevap:
        print("  --------  ")
        print("   \ O /|   ")
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
    elif tahmin!="kedi":
        print("yanlış tahmin oyun bitti öldünüz")
        print("     O_|    ")
        print("    /|\      ")
        print("    / \     ")
        break
    tahmin = input("tahmin yazınız..")
    if tahmin not in kelimeler:
        print("lütfen geçerli bir kelime giriniz..")
    elif tahmin==cevap:
        print("tebrikler doğru tahmin..")
        print("tahmininiz : {}\n cevap : {}".format(cevap,cevap))
        break








