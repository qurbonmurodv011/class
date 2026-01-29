# # 1-misol
# a=int(input("Sonni kiriting: "))
# for i in range(1,a+1):
#     print(i)

# # 2-misol
# a=["Ali", "Vali", "Hasan", "Malika", "Zuhra"]
# for i in a:
#     print(f"Salom {i}!")

# # 3-misol
# a=int(input("Sonni kiriting: "))
# b=[]
# for i in range(2,a+1,2):
#     b.append(i)
# print(*b)

# # 4-misol
# c=int(input("Sonni kiriting: "))
# b=0
# for a in range(1,c+1):
#     b+=a
# print(b)

# # 5-misol
# a=input("So'z kiriting: ")
# b=0
# for i in a:
#     i=1
#     b+=i
# print(b)

# # 6-misol
# a=int(input("Sonni kiriting: "))
# b=[]
# for i in range(3,a+1,3):
#     b.append(i)
# print(len(b))

# # 7-misol
# a=input("So'z kiriting: ")
# unli="aeiouаеёиоуыэю"
# b=0
# c=0
# for i in a:
#     if i.isalpha():
#         if i in unli:
#             b+=1
#         else:
#             c+=1
# print(f"Unlilar soni: {b}")
# print(f"Undoshlar soni: {c}")

# # 8-misol
# a = [23, 67, 12, 89, 45, 34, 91, 56, 78]
# b = a[0]
# for i in a:
#     if i>b:
#         i=b
#         print(b)
# print(b)

# # 9-masala
# a=input("Sonni kiriting: ")
# c=0
# for i in a:
#     b=int(i)
#     c+=b
# print(c)

# # 10-masala
# a=int(input("Sonni kiriting: "))
# b=0
# c=1
# for i in range(1,a+1):
#     c*=i
#     c+=b
# print(c)

# # 11-misol
# a = "MULTIPLIKATSIYA JADVALI"
# b = "=" * 60
# print(a)
# print(b)
# print("   |", end="")
# c = range(1, 11)
# for d in c:
#     print(f"{d:5}", end="")
# print()
# print("—" * 60)
# for e in c:
#     print(f"{e:2} |", end="")
#     for f in c:
#         print(f"{e * f:5}", end="")
#     print()

# # 12-misol
# h = int(input("Piramida balandligi: "))
# for i in range(1, h + 1):
#     for j in range(h - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()

# # 13-misol
# print("Fibonachchining birinchi 10 ta soni:")
# a = 0
# b = 1
# for i in range(10):
#     print(a, end=" ")
#     a, b = b, a + b

# # 14-misol
# a = []
# for b in range(2, 101):
#     c = True
#     for d in range(2, b):
#         if b % d == 0:
#             c = False
#             break
#     if c:
#         a.append(b)

# print("1 dan 100 gacha tub sonlar:")
# for e in a:
#     print(e, end=" ")
# print("\n\nJami:", len(a), "ta tub son")

# # 15-misol
# a = 0
# print("RAQAMLI SOAT SIMULYATORI")
# print("=" * 40)
#
# for b in range(24):          # soat (00–23)
#     for c in range(60):      # daqiqa (00–59)
#         for d in range(60):  # sekund (00–59)
#             print(f"{b:02}:{c:02}:{d:02}")
#             a += 1
#
# print("\nJami:", a, "ta vaqt")

# for i in range(1, 11):
#     print(i)
#     print(f"range()")

#  for tsikili - takrorlanish oldindan ma'lum
# for i in range(5):
#     print(i)
#   Natija: 0, 1, 2, 3, 4 (aniq 5 marta)
#
#   WHILE tsikili - takrorlanish shartga bog'liq
# i = 0
# while i < 10:
#     print(i)
#     i += 1
#  Natija: 0, 1, 2, 3, 4 5, 6, 7, 8, 9 (lekin necha marta takrorlanishi i ga bog'liq)

# x = input("Parolni kiritng: ")
#
# while x != "qwerty123":
#     print("Parol noto'g'ri, qayta urinib ko'ring.")
#     x = input("Parolni kiritng: ")
#     if x == "qwerty123":
#         print("Parol to'g'ri, xush kelibsiz!")
#         break

# i = 0
#
# while i < 10:
#      i += 1  # Bu qatorni AVVAL yozish kerak!
#
#      # Agar toq son bo'lsa - o'tkazib yubor
#      if i % 2 == 0: # Toq sonni tekshirish
#          continue # Keyingi kodlarni bajarmay, qaytadan input so'raymiz
#
#          print(i)

# def check_email(mail):
#     if "@" in mail:
#         return True
#     else:
#         return False
#
# email = input("e-mailni kiritng :")

# def yigindi(*son): # *args - Arguments
#
#     jami = 0
#     for son in son:
#         jami += son
#     return jami
#
# print(yigindi(1, 2, 3, 10, 100, 1000))

# number = int(input("Raqam kirintg: "))
#
# if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
# elif number % 5 == 0:
#     print("Buzz")
# elif number % 3 == 0:
#     print("Fizz")
# else:
#     print(number)

class Mashina:
    def __init__(self, rang, model, tezlik):
        self.rang = rang
        self.model = model
        self.tezlik = tezlik
    # metod yaratamiz
    # 1-metod gaz_ber
    def gaz_ber(self, miqdor):
        self.tezlik += miqdor

    # 2-metod tormozla metodi
    def tormozla(self, miqdor):
        self.tezlik -= miqdor
        if self.tezlik < 0:
            self.tezlik = 0

Equinox = Mashina("Qora","Premier", 220)
Malibu = Mashina("Oq", "XL", 260)
Cobalt = Mashina("Qora", "Ltz",250)


Cobalt.gaz_ber(50)
Cobalt.tormozla(400)
print(f"Cobalt modeli: {Cobalt.model}\nCobalt rangi: {Cobalt.rang}\nCobalt tezligi: {Cobalt.tezlik}km/s")


# def yigindi(son1, son2):
#     natija = son1 + son2
#     return natija

# x = int(input("1-sonni kiritng: "))
# y = int(input("2-sonni kirintg: "))

# print(f"Yig'indisi: {yigindi(x, y)}")

# def summa(a, b):
#     print(f"{a} + {b} = {a + b}")

# summa(3, 5) # Natija: 3 + 5 =8
# summa(10, 20) # Natija: 10 + 20 = 30


# def salom_ayt(ism ="do'stim"):
#     print(f"Salom, {ism}!")

#     salom_ayt()        # Natija: Salom, do'stim!
#     salom_ayt("Ali")    # Natija: Salom, Ali !7

# def bolani_malumotlari(ism,yosh):
#     print(f"{ism} {yosh} yoshda.")
#
#
# bolani_malumotlari(ism="Ali", yosh=11)  # Natija: Ali 11 yoshda.
# bolani_malumotlari(yosh=12, ism="Vali")  # Natija: Vali 12 yoshda.


# def min_max(sonlar):
#     return min(sonlar), max(sonlar)
#
# kichik, katta = min_max([1, 2, 3, 4, 5,])
# print(f"Eng kichik: {kichik}, Eng katta: {katta}")  # Natija: Eng kichik: 1, Eng katta: 5


class Transport:
    def __init__(self, model: str, yil: int) -> None:
        self.model = model
        self.yil = yil

    def malumot(self) -> str:
        return f"Model: {self.model}, Yil: {self.yil}"


class Avtomobil(Transport):
    def __init__(self, model: str, yil: int, yonilgi_turi: str) -> None:
        # Ota klassning __init__ metodini chaqirish
        super().__init__(model, yil)
        self.yonilgi_turi = yonilgi_turi

    def malumot(self) -> str:
        # Ota klassdagi metod natijasiga qo'shimcha qo'shish
        return super().malumot() + f", Yonilg'i: {self.yonilgi_turi}"


class Avtobus(Transport):
    def __init__(self, model: str, yil: int, o_rinlar_soni: int) -> None:
        # Ota klassning __init__ metodini chaqirish
        super().__init__(model, yil)
        self.o_rinlar_soni = o_rinlar_soni

    def malumot(self) -> str:
        # Ota klassdagi metod natijasiga qo'shimcha qo'shish
        return super().malumot() + f", O'rinlar: {self.o_rinlar_soni}"


# Tekshirish uchun namunalar:
avto = Avtomobil("Tesla Model S", 2023, "Elektr")
avtobus = Avtobus("Isuzu", 2021, 35)

print(avto.malumot())
print(avtobus.malumot())

