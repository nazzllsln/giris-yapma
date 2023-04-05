def giris():
    print("-Welcome to PYTHON Bank(v.0.1)-")
    print("1.Login")
    print("2.Exit")
    sayi = int(input())
    while sayi <= 2 and sayi > 0:
        if sayi == 1:
            Username = input("Username: ")
            Password = int(input("Password: "))
            if Username == "Ahmet" and Password == 1234:
                print("Giriş Başarılı")
                print("WELCOME ",Username)
                break
            elif Username == "Zeynep" and Password == 4321:
                print("Giriş Başarılı")
                print("WELCOME ", Username)
                break
            else:
                print("Kullanıcı adı veya şifre hatalı lütfen tekrar deneyiniz.")
        else:
            giris()


giris()